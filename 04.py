from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        qty_days_to_birthday = (birthday_this_year - today).days

        if 0 <= qty_days_to_birthday <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() in (5, 6):
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John", "birthday": "1985.01.23"},
    {"name": "Jane", "birthday": "1990.01.27"},
    {"name": "Emily", "birthday": "1987.07.12"},
    {"name": "Michael", "birthday": "1991.07.13"},
    {"name": "Linda", "birthday": "1988.07.14"},
    {"name": "Linda", "birthday": "1988.07.20"},
    {"name": "Antony", "birthday": "1982.04.27"},
    {"name": "Evan", "birthday": "2000.06.25"},
    {"name": "Tom", "birthday": "1995.04.25"},
    {"name": "Mac", "birthday": "1990.12.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
