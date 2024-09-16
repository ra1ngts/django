import asyncio
from datetime import datetime

import aiohttp

from init_db import fetch_weather_data, db_run

# The Open-Meteo API settings
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 55.69783233134807,
    "longitude": 37.35957755503296,
    "current": ["temperature_2m", "precipitation", "pressure_msl", "wind_speed_10m", "wind_direction_10m"],
    "wind_speed_unit": "ms",
    "timezone": "Europe/Moscow",
    "forecast_days": 1
}


async def get_api_data(api_url: str, parameters: dict, timeout: int = 10) -> dict:
    """
    Функция отправляет запрос к API для получения данных о погоде.
    Параметры:
        - api_url (str): URL API.
        - parameters (dict): Параметры запроса.
        - timeout (int): Таймаут запроса в секундах.
    Возвращает:
        - dict: Данные о погоде в формате JSON.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url=api_url, params=parameters, timeout=timeout) as response:
                response.raise_for_status()
                return await response.json()
        except asyncio.TimeoutError:
            return {"error": "Запрос истек по времени."}
        except aiohttp.ClientError as e:
            return {"error": f"Ошибка запроса: {e}"}


async def get_abbreviation(number: float | int) -> str:
    """
    Функция определяет аббревиатуру направления ветра на основе угла в градусах.
    Параметры:
        - number (float | int): Угол направления ветра в градусах (0-360).
    Возвращает:
        - str: Аббревиатура направления ветра.
    """
    if 0 <= number < 45:
        return "СВ"
    elif number == 45:
        return "СВ"
    elif 45 < number < 90:
        return "ВСВ"
    elif number == 90:
        return "В"
    elif 90 < number < 135:
        return "ВЮВ"
    elif number == 135:
        return "ЮВ"
    elif 135 < number < 180:
        return "ЮЮВ"
    elif number == 180:
        return "Ю"
    elif 180 < number < 225:
        return "ЮЮЗ"
    elif number == 225:
        return "ЮЗ"
    elif 225 < number < 270:
        return "ЗЮЗ"
    elif number == 270:
        return "З"
    elif 270 < number < 315:
        return "ЗСЗ"
    elif number == 315:
        return "СЗ"
    elif 315 < number <= 360:
        return "ССЗ"
    else:
        return "Неверное значение направления ветра"


async def get_weather_data(engine):
    """
    Функция получает данные о погоде, делает необходимые преобразования и
    записывает данные в БД, а так же распечатывает их в консоль.
    Параметры:
        - engine (Engine): Объект, осуществляющий подключение к базе данных.
    """
    weather_data = await get_api_data(url, params)

    if "error" in weather_data:
        print(weather_data["error"])
    else:
        current = weather_data.get("current")
        current_temperature_2m = current.get("temperature_2m", "Нет данных")
        current_wind_direction_10m = current.get("wind_direction_10m", "Нет данных")
        current_wind_speed_10m = current.get("wind_speed_10m", "Нет данных")
        current_pressure_msl = current.get("pressure_msl", "Нет данных")
        current_precipitation = current.get("precipitation", "Нет данных")

        abbreviation = await get_abbreviation(current_wind_direction_10m)  # Получаем аббревиатуру направления ветра
        pressure_to_mm = current_pressure_msl * 0.75  # Переводим hPa в мм рт/ст

        fetch_weather_data(
            engine=engine,
            temperature=round(current_temperature_2m, 1),
            wind_direction=abbreviation,
            wind_speed=round(current_wind_speed_10m, 2),
            pressure=round(pressure_to_mm),
            precipitation=current_precipitation,
        )

        print(f"Температура в C°     | {round(current_temperature_2m, 1)}")
        print(f"Направление ветра    | {abbreviation}")
        print(f"Скорость ветра в м/с | {round(current_wind_speed_10m, 2)}")
        print(f"Давление в мм рт/ст  | {round(pressure_to_mm)}")
        print(f"Осадки в мм          | {current_precipitation}")
        print(f"Текущая дата и время | {datetime.now()}")


async def main():
    """
    Функция отвечает за выполнение основного скрипта (сбор данных о погоде и их выгрузка в БД с заданным интервалом).
    Действия:
        - db_run(): Запуск и подключение к базе данных.
        - get_weather_data(): Сбор данных о погоде и запись их в базу данных.
        - asyncio.sleep(): Ожидание перед следующим циклом выгрузки данных.
    Выгрузка данных происходит каждые: 15 секунд.
    """
    engine = db_run()

    while True:
        await get_weather_data(engine)
        await asyncio.sleep(15)  # Задержка каждые 15 сек
        print("---")


if __name__ == "__main__":
    asyncio.run(main())
