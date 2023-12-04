import psycopg2

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
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_all_vacancies(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""SELECT  title, company_name, payment_from, link_ FROM vacancies
                        JOIN employers USING(employer_id)
           """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_avg_salary(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""SELECT  ROUND(AVG(payment_from)) AS average_payment FROM vacancies
           """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_vacancies_with_higher_salary(self):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""SELECT title, payment_from FROM vacancies
                        WHERE payment_from > (SELECT AVG(payment_from) FROM vacancies)
                        ORDER BY payment_from
           """)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_vacancies_with_keyword(self, keyword):
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(f"SELECT title FROM vacancies WHERE title LIKE '%{keyword}%'"
           )
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result


