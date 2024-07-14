from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        date_in_past = datetime.strptime(date, "%Y-%m-%d").date()
        print(date_in_past)
        current_date = datetime.today().date()
        difference = date_in_past - current_date
        return difference.days
    except ValueError:
        print("Invalid format date. You must use format 'YYYY-MM-DD'.")
        return None


print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2021-10-09'))
print(get_days_from_today('2021-10'))
