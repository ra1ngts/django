import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_file_path = BASE_DIR / "forecast/config" / "db_settings.yaml"


def get_config(path):
    """
    Функция загрузки конфигурации из YAML файла.
    Параметры:
        path (str): Путь к файлу конфигурации.
    Возвращает:
        dict: Данные конфигурации, загруженные из YAML файла (параметры подключения к БД).
    """
    with open(path) as f:
        configuration = yaml.safe_load(f)
    return configuration


config = get_config(config_file_path)
