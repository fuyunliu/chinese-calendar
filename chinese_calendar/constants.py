import datetime
from enum import Enum, auto


class Holiday(Enum):

    New_Years_Day = auto()  # 元旦节
    New_Years_Eve = auto()  # 除夕
    Spring_Festival = auto()  # 春节
    Tomb_Sweeping_Day = auto()  # 清明节
    Labour_Day = auto()  # 劳动节
    Dragon_Boat_Festival = auto()  # 端午节
    Mid_Autumn_Festival = auto()  # 中秋节
    National_Day = auto()  # 国庆节


class Lieuday(Enum):
    Lieu_Day = auto()  # 调休日


holidays = {
    datetime.date(year=2020, month=1, day=1): Holiday.New_Years_Day.value,

    datetime.date(year=2020, month=1, day=24): Holiday.New_Years_Eve.value,
    datetime.date(year=2020, month=1, day=25): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=1, day=26): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=1, day=27): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=1, day=28): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=1, day=29): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=1, day=30): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=1, day=31): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=2, day=1): Holiday.Spring_Festival.value,
    datetime.date(year=2020, month=2, day=2): Holiday.Spring_Festival.value,

    datetime.date(year=2020, month=4, day=4): Holiday.Tomb_Sweeping_Day.value,
    datetime.date(year=2020, month=4, day=5): Holiday.Tomb_Sweeping_Day.value,
    datetime.date(year=2020, month=4, day=6): Holiday.Tomb_Sweeping_Day.value,

    datetime.date(year=2020, month=5, day=1): Holiday.Labour_Day.value,
    datetime.date(year=2020, month=5, day=2): Holiday.Labour_Day.value,
    datetime.date(year=2020, month=5, day=3): Holiday.Labour_Day.value,
    datetime.date(year=2020, month=5, day=4): Holiday.Labour_Day.value,
    datetime.date(year=2020, month=5, day=5): Holiday.Labour_Day.value,

    datetime.date(year=2020, month=6, day=25): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2020, month=6, day=26): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2020, month=6, day=27): Holiday.Dragon_Boat_Festival.value,

    datetime.date(year=2020, month=10, day=1): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=2): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=3): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=4): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=5): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=6): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=7): Holiday.National_Day.value,
    datetime.date(year=2020, month=10, day=8): Holiday.National_Day.value,

    datetime.date(year=2019, month=1, day=1): Holiday.New_Years_Day.value,

    datetime.date(year=2019, month=2, day=4): Holiday.New_Years_Eve.value,
    datetime.date(year=2019, month=2, day=5): Holiday.Spring_Festival.value,
    datetime.date(year=2019, month=2, day=6): Holiday.Spring_Festival.value,
    datetime.date(year=2019, month=2, day=7): Holiday.Spring_Festival.value,
    datetime.date(year=2019, month=2, day=8): Holiday.Spring_Festival.value,
    datetime.date(year=2019, month=2, day=9): Holiday.Spring_Festival.value,
    datetime.date(year=2019, month=2, day=10): Holiday.Spring_Festival.value,

    datetime.date(year=2019, month=4, day=5): Holiday.Tomb_Sweeping_Day.value,
    datetime.date(year=2019, month=4, day=6): Holiday.Tomb_Sweeping_Day.value,
    datetime.date(year=2019, month=4, day=7): Holiday.Tomb_Sweeping_Day.value,

    datetime.date(year=2019, month=5, day=1): Holiday.Labour_Day.value,
    datetime.date(year=2019, month=5, day=2): Holiday.Labour_Day.value,
    datetime.date(year=2019, month=5, day=3): Holiday.Labour_Day.value,
    datetime.date(year=2019, month=5, day=4): Holiday.Labour_Day.value,

    datetime.date(year=2019, month=6, day=7): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2019, month=6, day=8): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2019, month=6, day=9): Holiday.Dragon_Boat_Festival.value,

    datetime.date(year=2019, month=9, day=13): Holiday.Mid_Autumn_Festival.value,
    datetime.date(year=2019, month=9, day=14): Holiday.Mid_Autumn_Festival.value,
    datetime.date(year=2019, month=9, day=15): Holiday.Mid_Autumn_Festival.value,

    datetime.date(year=2019, month=10, day=1): Holiday.National_Day.value,
    datetime.date(year=2019, month=10, day=2): Holiday.National_Day.value,
    datetime.date(year=2019, month=10, day=3): Holiday.National_Day.value,
    datetime.date(year=2019, month=10, day=4): Holiday.National_Day.value,
    datetime.date(year=2019, month=10, day=5): Holiday.National_Day.value,
    datetime.date(year=2019, month=10, day=6): Holiday.National_Day.value,
    datetime.date(year=2019, month=10, day=7): Holiday.National_Day.value,

    datetime.date(year=2018, month=1, day=1): Holiday.New_Years_Day.value,
    datetime.date(year=2018, month=2, day=15): Holiday.New_Years_Eve.value,
    datetime.date(year=2018, month=2, day=16): Holiday.Spring_Festival.value,
    datetime.date(year=2018, month=2, day=17): Holiday.Spring_Festival.value,
    datetime.date(year=2018, month=2, day=18): Holiday.Spring_Festival.value,
    datetime.date(year=2018, month=2, day=19): Holiday.Spring_Festival.value,
    datetime.date(year=2018, month=2, day=20): Holiday.Spring_Festival.value,
    datetime.date(year=2018, month=2, day=21): Holiday.Spring_Festival.value,

    datetime.date(year=2018, month=4, day=5): Holiday.Tomb_Sweeping_Day.value,
    datetime.date(year=2018, month=4, day=6): Holiday.Tomb_Sweeping_Day.value,
    datetime.date(year=2018, month=4, day=7): Holiday.Tomb_Sweeping_Day.value,

    datetime.date(year=2018, month=4, day=29): Holiday.Labour_Day.value,
    datetime.date(year=2018, month=4, day=30): Holiday.Labour_Day.value,
    datetime.date(year=2018, month=5, day=1): Holiday.Labour_Day.value,

    datetime.date(year=2018, month=6, day=16): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=6, day=17): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=6, day=18): Holiday.Dragon_Boat_Festival.value,

    datetime.date(year=2018, month=9, day=22): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=9, day=23): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=9, day=24): Holiday.Dragon_Boat_Festival.value,

    datetime.date(year=2018, month=10, day=1): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=10, day=2): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=10, day=3): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=10, day=4): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=10, day=5): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=10, day=6): Holiday.Dragon_Boat_Festival.value,
    datetime.date(year=2018, month=10, day=7): Holiday.Dragon_Boat_Festival.value,

    datetime.date(year=2018, month=12, day=30): Holiday.New_Years_Day.value,
    datetime.date(year=2018, month=12, day=31): Holiday.New_Years_Day.value,

}


lieudays = {
    datetime.date(year=2020, month=1, day=19): Lieuday.Lieu_Day.value,
    datetime.date(year=2020, month=4, day=26): Lieuday.Lieu_Day.value,
    datetime.date(year=2020, month=5, day=9): Lieuday.Lieu_Day.value,
    datetime.date(year=2020, month=6, day=28): Lieuday.Lieu_Day.value,
    datetime.date(year=2020, month=9, day=27): Lieuday.Lieu_Day.value,
    datetime.date(year=2020, month=10, day=10): Lieuday.Lieu_Day.value,

    datetime.date(year=2019, month=2, day=2): Lieuday.Lieu_Day.value,
    datetime.date(year=2019, month=2, day=3): Lieuday.Lieu_Day.value,
    datetime.date(year=2019, month=4, day=28): Lieuday.Lieu_Day.value,
    datetime.date(year=2019, month=5, day=5): Lieuday.Lieu_Day.value,
    datetime.date(year=2019, month=9, day=29): Lieuday.Lieu_Day.value,
    datetime.date(year=2019, month=10, day=12): Lieuday.Lieu_Day.value,

    datetime.date(year=2018, month=2, day=11): Lieuday.Lieu_Day.value,
    datetime.date(year=2018, month=2, day=24): Lieuday.Lieu_Day.value,
    datetime.date(year=2018, month=4, day=8): Lieuday.Lieu_Day.value,
    datetime.date(year=2018, month=4, day=28): Lieuday.Lieu_Day.value,
    datetime.date(year=2018, month=9, day=29): Lieuday.Lieu_Day.value,
    datetime.date(year=2018, month=9, day=30): Lieuday.Lieu_Day.value,
    datetime.date(year=2018, month=12, day=29): Lieuday.Lieu_Day.value,
}
