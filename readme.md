# Курсовая работа 5. Работа с базами данных

Программа получает данные о работодателях и их вакансиях с сайта hh.ru. Для этого используется публичный API hh.ru и библиотека 
requests
.
Данные берутся из 10 компаний, адреса которых прописаны в списке emploeer_ids в файле main.py.
Программа создает таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используйтся библиотека 
psycopg2. Для подключения к базе данных необходимо самостоятельно создать файл database.ini по образцу, который приложен к проекту - database.ini.example
.

## Работа с БД PostgreSQL

В программе реализован код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
Создан класс DBManager  для работы с данными в БД.

### Работа программы

При запуске программы начинается парсинг сайта hh.ru, при этом программа информирует о полученных данных о работодателях и вакансиях.
После этого бесконечным циклом предлагаются действия. 

Для завершение работы нажать 0