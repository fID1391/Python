
class DateInitError(Exception):
    pass


class Date:

    def __init__(self, date):
        try:
            date = self.parse_date(date)
            date = self.checked_date(date)
        except ValueError:
            raise DateInitError("Неверный формат даты")
        else:
            self.date = date

    @classmethod
    def parse_date(cls, date):
        result = [int(item) for item in date.split("-")]
        if len(result) != 3:
            raise ValueError
        return result

    @staticmethod
    def checked_date(date):
        day, month, year = date
        if (1 <= day <= 31) and (1 <= month <= 12) and (1 <= year <= 2021):
            return day, month, year
        else:
            raise ValueError

    def __str__(self):
        return f"{self.date[2]}.{self.date[1]}.{self.date[0]}"


lst_date = ["31-12-2021", "32-12-2022", "12-12--2022"]
for date in lst_date:
    try:
        print(Date(date))
    except DateInitError as e:
        print(f"Дата: {date}, ошибка: '{e}'")

