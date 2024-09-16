from sqlalchemy import (
    MetaData, Table, Column,
    Integer, String, Date
)

meta = MetaData()

weather = Table(
    "weather", meta,
    Column("id", Integer, primary_key=True),  # Номер записи
    Column("temperature", String(50), nullable=False),  # Температура
    Column("wind_direction", String(50), nullable=False),  # Направление ветра
    Column("wind_speed", String(50), nullable=False),  # Скорость ветра
    Column("pressure", String(50), nullable=False),  # Давление
    Column("precipitation", String(50), nullable=False),  # Осадки
    Column("date", Date, nullable=False)  # Дата
)
