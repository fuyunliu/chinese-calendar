import datetime

from . import constants as cs


def is_weekday(date):
    """
    判断是否为平常日，周一至周五
    """
    return 1 <= date.isoweekday() <= 5


def is_weekend(date):
    """
    判断是否为周末日，周六和周日
    """
    return 6 <= date.isoweekday() <= 7


def is_holiday(date):
    """
    判断是否为节假日，放假的日子
    """
    return date in cs.holidays


def is_workday(date):
    """
    判断是否为工作日，需要上班的日子
    """
    return (is_weekday(date) and not is_holiday(date)) or is_lieuday(date)


def is_restday(date):
    """
    判断是否为休息日，排除调休日的周末
    """
    return is_weekend(date) and not is_lieuday(date)


def is_lieuday(date):
    """
    判断是否为调休日，调休上班的日子
    """
    return date in cs.lieudays