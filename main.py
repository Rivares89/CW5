import os

from utils import get_emploeers, get_vacancies, create_database, save_data_to_database
from config import config
from DBmanager import DBmanager


def main():
    url = "https://api.hh.ru"
    # emploeer_ids = [1740, 4006]
    emploeer_ids = [1740, 15478, 8620, 3529, 78638, 4006, 4504679, 561525, 64174, 8642172]
    params = config()

    data_emploeers = get_emploeers(url, emploeer_ids)
    data_vacancies = get_vacancies(url, emploeer_ids)
    create_database('hh', params)
    save_data_to_database(data_emploeers, data_vacancies, 'hh', params)

    while True:
        user_input = input("Выберите действие программы: \n"
                           "1 - получает список всех компаний и количество вакансий у каждой компании\n"
                           "2 - получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
                           "3 - получает среднюю зарплату по вакансиям\n"
                           "4 - получает список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
                           "5 - получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python\n"
                           "0 - завершение работы\n")
        db = DBmanager('hh', params)
        if user_input == 0:
            break
        elif user_input == 1:
            print(db.get_companies_and_vacancies_count())
        elif user_input == 2:
            print(db.get_all_vacancies())
        elif user_input == 3:
            print(db.get_companies_and_vacancies_count())
        elif user_input == 4:
            print(db.get_companies_and_vacancies_count())
        elif user_input == 5:
            print(db.get_companies_and_vacancies_count())
        elif user_input == 6:
            print(db.get_companies_and_vacancies_count())




if __name__ == '__main__':
    main()

