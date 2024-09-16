import asyncio

import pandas as pd
import asyncpg

from settings import config

excel_file_path = "data_from_db.xlsx"


async def connection_to_db():
    """
    Функция подключения к базе данных, выполнения SQL-запроса для извлечения данных о погоде
    и экспорта полученных данных в XLSX файл.
    Действия:
        - Подключение к базе данных через asyncpg.
        - Выполнение SQL-запроса для получения последних 10 записей из таблицы weather.
        - Создание DataFrame из полученных данных.
        - Экспорт данных в XLSX файл.
    """
    connection = await asyncpg.connect(
        user=config["postgres"]["user"],
        password=str(config["postgres"]["password"]),
        database=config["postgres"]["database"],
        host=config["postgres"]["host"],
        port=str(config["postgres"]["port"])
    )
    print(f"Подключено к БД: '{config["postgres"]["database"]}'.")

    try:
        query = "SELECT * FROM weather ORDER BY id DESC LIMIT 10"
        result = await connection.fetch(query)

        columns = result[0].keys() if result else []
        data_frame = pd.DataFrame([dict(row) for row in result], columns=columns)
        print(data_frame.head())

        data_frame.to_excel(excel_file_path, index=False)
        print(f"Данные успешно выгружены в '{excel_file_path}'.")
        await connection.close()
    except Exception as e:
        print(f"Ошибка при выполнении запроса или экспорте данных: {e}")


if __name__ == "__main__":
    asyncio.run(connection_to_db())
