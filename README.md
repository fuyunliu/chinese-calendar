# 中国节假日

## 安装

```sh
pip install chinese-calendar
```

## 用法

```python
import datetime
import chinese_calendar

# 判断是否为平常日，周一至周五
chinese_calendar.is_weekday(datetime.date(year=2020, month=1, day=10))  # True

# 判断是否为周末日，周六和周日
chinese_calendar.is_weekend(datetime.date(year=2020, month=1, day=12))  # True

# 判断是否为节假日，放假的日子
chinese_calendar.is_holiday(datetime.date(year=2020, month=1, day=1))  # True

# 判断是否为工作日，需要上班的日子
chinese_calendar.is_workday(datetime.date(year=2020, month=1, day=17))  # True

# 判断是否为休息日，排除调休日的周末
chinese_calendar.is_restday(datetime.date(year=2020, month=1, day=5))  # True

# 判断是否为调休日，调休上班的日子
chinese_calendar.is_lieuday(datetime.date(year=2020, month=1, day=19))  # True

```
