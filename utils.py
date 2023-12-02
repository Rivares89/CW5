import requests
from exception import ParsingError
from datetime import datetime

def get_emploeers(url, emploeer_ids):
    '''Получение данных о работодателях с hh.ru'''
    hh_companies = []
    for employer_id in emploeer_ids:
        response = requests.get(f'{url}/employers/{employer_id}')
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        data = response.json()
        hh_company = {
            "employer_id": int(employer_id),
            "company_name": data['name'],
            "open_vacancies": data['open_vacancies']
        }
        hh_companies.extend(hh_company)
    print(hh_companies)

def get_vacancies(url, emploeer_ids):
    '''Получение данных о вакансиях с hh.ru'''
    params = {
        'area': 1,
        'page': 0,
        'per_page': 10
    }
    formatted_vacancies = []
    vacancies = []
    for employer_id in emploeer_ids:
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
    print(formatted_vacancies)




def create_database(database_name, params):
    '''Создание базы данных и таблиц'''

def save_data_to_database(data, database_name, params):
    '''Сохранение данных в базу данных'''
