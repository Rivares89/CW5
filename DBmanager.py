import psycopg2
from poetry.console.commands import self

from config import config

class DBmanager:
    '''Класс для работы с базой данных'''
    def __init__(self, database_name, params):
        self.database_name = database_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""SELECT company_name, COUNT(title) FROM employers
                        JOIN vacancies USING(employer_id)
                        GROUP BY company_name
           """)
        conn.commit()
        conn.close()
