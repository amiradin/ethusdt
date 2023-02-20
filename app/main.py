# std
import requests

# local
import utils as utils
from constants import ETH_USDT, FIELD_BUY


def main():
    """
    Главная функция для запуска программы
    """
    value = get_ticker()
    print(f"Цена при запуске программы: {value}")
    time_update = utils.get_time_now()
    while True:
        time_now = utils.get_time_now()
        if time_now - 3600 > time_update:
            time_update = utils.get_time_now()
            updated_value = get_ticker()
            if utils.difference(value, updated_value):
                print("Изменение цены!")
            else:
                pass
        else:
            pass


def get_ticker():
    """
    Функция получения данных через API
    """
    try:
        response = requests.get(url=f"https://yobit.net/api/3/ticker/eth_usdt")
    except Exception as e:
        raise e
    data = dict(response.json())
    return data[ETH_USDT][FIELD_BUY]


if __name__ == "__main__":
    print("Start server...")
    main()
