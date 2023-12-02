
import json
from abc import ABC, abstractmethod
# from datetime import datetime
# from config import API_KEY
from exception import ParsingError
import requests

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    # @abstractmethod
    # def get_vacancies(self):
    #     pass

class HeadHunter(Engine):
    #url = "https://api.hh.ru/employer/8915586"
    url = "https://api.hh.ru"

    def __init__(self, keyword):
        self.params = {
            # "text": keyword,
            # "page": None,
            # "per_page": 3
        }
        self.vacancies = []
        self.employer = []

    def get_request(self):
        '''Делает запрос и возвращает в формате json'''
        response = requests.get(f'{self.url}/employer/3754394', params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        print(response.json())


    # def get_vacancies(self, pages_count=2):
    #     '''Проходим циклом по словарю  записываем данные в переменную "vacancies" '''
    #     self.vacancies = [] # очищаем список
    #     for page in range(pages_count):
    #         page_vacancies = []
    #         print(f"({self.__class__.__name__}) Парсинг страницы {page} -", end=" ")
    #         try:
    #             page_vacancies = self.get_request()
    #         except ParsingError as error:
    #             print(error)
    #         else:
    #             self.vacancies.extend(page_vacancies['items'])
    #             print(f"Загружено вакансий {len(page_vacancies['items'])}")
    #         if len(page_vacancies) == 0:
    #             break
    #
    # def get_formatted_vacancies(self):
    #     '''Проходим циклом по данным, записанным в self.vacancies и берем только нужные нам данные и записываем в formatted_vacancies'''
    #     formatted_vacancies = []
    #     for vacancy in self.vacancies:
    #         published_at = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S%z")
    #         formatted_vacancy = {
    #             "employer": vacancy['department']['name'] if vacancy.get('department') else None,
    #             "title": vacancy['name'],
    #             "payment_from": vacancy['salary']['from'] if vacancy.get('salary') else None,
    #             "payment_to": vacancy['salary']['to'] if vacancy.get('salary') else None,
    #             'responsibility': vacancy['snippet']['responsibility'],
    #             'link': vacancy['apply_alternate_url'],
    #             'date': published_at.strftime("%d.%m.%Y"),
    #         }
    #         formatted_vacancies.append(formatted_vacancy)
    #     return formatted_vacancies

#
# class HeadHunter:
#     url = "https://api.hh.ru/vacancy/90028367"
#
#     def __init__(self, keyword):
#         self.params = {
#             "text": keyword,
#             "page": None,
#             "per_page": 5
#         }
#         self.vacancies = []
#
#     # https: // hh.ru / vacancy / 90028367