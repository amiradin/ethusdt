from time import time
from constants import PERCENT


def get_time_now() -> int:
    """
    Возращает текущее время в UNIXTIME
    """
    return int(time())


def difference(start_value, updated_value) -> bool:
    """
    Вычиление разницы и уведомление
    """
    start_percent = start_value / 100 * PERCENT
    return (
        False
        if start_value - start_percent < updated_value < start_value + start_percent
        else True
    )
