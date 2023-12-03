import os

from utils import get_emploeers, get_vacancies, create_database, save_data_to_database
from config import config


def main():
    url = "https://api.hh.ru"
    emploeer_ids = [1740, 4006]
    # emploeer_ids = [1740, 15478, 8620, 3529, 78638, 4006, 4504679, 561525, 64174, 8642172]
    params = config()

    data_emploeers = get_emploeers(url, emploeer_ids)
    data_vacancies = get_vacancies(url, emploeer_ids)
    create_database('hh', params)
    save_data_to_database(data_emploeers, data_vacancies, 'hh', params)


if __name__ == '__main__':
    main()

