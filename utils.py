import requests
from exception import ParsingError
from datetime import datetime
import psycopg2

def get_emploeers(url, emploeer_ids):
    '''Получение данных о работодателях с hh.ru'''
    hh_companies = []
    count = 1
    for employer_id in emploeer_ids:
        response = requests.get(f'{url}/employers/{employer_id}')
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        data = response.json()
        print(f'Получено {count} работодателей из {len(emploeer_ids)}')
        count += 1
        hh_company = {
            "employer_id": int(employer_id),
            "company_name": data['name'],
            "open_vacancies": data['open_vacancies']
        }
        hh_companies.extend(hh_company)
    return hh_companies

def get_vacancies(url, emploeer_ids):
    '''Получение данных о вакансиях с hh.ru'''
    params = {
        'area': 1,
        'page': 0,
        'per_page': 10
    }

    formatted_vacancies = []
    for employer_id in emploeer_ids:
        vacancies = []
        response = requests.get(f'{url}/vacancies?employer_id={employer_id}', params=params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        page_vacancies = response.json()
        vacancies.extend(page_vacancies["items"])
        for vacancy in vacancies:
            published_at = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S%z")
            formatted_vacancy = {
                "employer": vacancy['department']['name'] if vacancy.get('department') else None,
                "title": vacancy['name'],
                "payment_from": vacancy['salary']['from'] if vacancy.get('salary') else None,
                "payment_to": vacancy['salary']['to'] if vacancy.get('salary') else None,
                'responsibility': vacancy['snippet']['responsibility'],
                'link': vacancy['apply_alternate_url'],
                'date': published_at.strftime("%d.%m.%Y"),
            }
            formatted_vacancies.append(formatted_vacancy)
            print(f'Получено {len(formatted_vacancies)} вакансий')

    return formatted_vacancies

def create_database(database_name, params):
    '''Создание базы данных и таблиц'''
    conn = psycopg2.connection(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connection(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE emploeers (
        employer_id PRIMARY KEY,
        company_name VARCHAR,
        open_vacancies INTEGER
        )
        """)

    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE vacancies (
        vacancy_id SERIAL PRIMARY KEY,
        employer VARCHAR REFERENCES emploeers(company_name),
        title TEXT,
        payment_from INTEGER,
        payment_to INTEGER,
        responsibility TEXT,
        link TEXT,
        date DATE,
        )
        """)

    conn.commit()
    conn.close()

def save_data_to_database(data_emploeers, data_vacancies, database_name, params):
    '''Сохранение данных в базу данных'''

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for employer in data_emploeers:
            cur.execute("""
            INSERT INTO emploeers (employer_id, company_name, open_vacancies)
            VALUES (%s, %s, %s)
            RETURNING
            """,
                        (employer['employer_id'], employer['company_name'], employer['open_vacancies'])
            )

        for vacancy in data_vacancies:
            cur.execute("""
            INSERT INTO vacancies (vacancy_id, employer, title, payment_from, payment_to, responsibility, link, date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING
            """,
                        (vacancy['vacancy_id'], vacancy['employer'],
                         vacancy['title'], vacancy['payment_from'], vacancy['payment_to'],
                         vacancy['responsibility'], vacancy['link'], vacancy['date'])
            )