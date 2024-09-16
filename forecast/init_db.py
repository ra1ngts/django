from sqlalchemy import create_engine, MetaData
from datetime import datetime

from settings import config
from db import weather

# Data Source Name
DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    """
    Функция создания таблиц в базе данных.
    Параметры:
        - engine (Engine): Объект, осуществляющий подключение к базе данных.
    """
    meta = MetaData()
    meta.create_all(bind=engine, tables=[weather])


def fetch_weather_data(engine, temperature, wind_direction, wind_speed, pressure, precipitation):
    """
    Функция добавления записи о погоде в базу данных.
    Параметры:
        - engine (Engine): Объект, осуществляющий подключение к базе данных.
        - temperature (str): Значение температуры.
        - wind_direction (str): Направление ветра.
        - wind_speed (str): Скорость ветра.
        - pressure (str): Атмосферное давление.
        - precipitation (str): Осадки.
        - date (date): Текущая дата.
    """
    conn = engine.connect()
    conn.execute(weather.insert(), [
        {"temperature": temperature,
         "wind_direction": wind_direction,
         "wind_speed": wind_speed,
         "pressure": pressure,
         "precipitation": precipitation,
         "date": datetime.today().date()}
    ])
    conn.commit()
    conn.close()


def db_run():
    """
    Функция запуска процесса работы с базой данных.
    Осуществляет подключение к базе данных и создание таблиц.
    Возвращает:
        - engine (Engine): Объект, осуществляющий подключение к базе данных.
    """
    db_url = DSN.format(**config["postgres"])
    engine = create_engine(db_url)
    create_tables(engine)
    return engine
