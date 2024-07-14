## Technical Task Description

### Task 1
Create a function `get_days_from_today(date)` that calculates the number of days between a given date and the current date.

#### Task Requirements:
- The function takes one parameter: `date`—a string representing the date in the format 'YYYY-MM-DD' (e.g., '2020-10-09').
- The function returns an integer indicating the number of days from the given date to the current date. If the given date is later than the current date, the result should be negative.
- The calculation should consider only days, ignoring time (hours, minutes, seconds).
- The `datetime` module in Python should be used to work with dates.

#### Recommendations:
1. Import the `datetime` module.
2. Convert the date string in 'YYYY-MM-DD' format to a `datetime` object.
3. Get the current date using `datetime.today()`.
4. Calculate the difference between the current date and the given date.
5. Return the difference in days as an integer.

#### Evaluation Criteria:
- Function correctness: the function should accurately calculate the number of days between dates.
- Exception handling: the function should handle incorrect input data formats.
- Code readability: the code should be clean and well-documented.

#### Example:
If today is May 5, 2021, calling `get_days_from_today("2021-10-09")` should return 157, since October 9, 2021, is 157 days after May 5, 2021.

### Task 2
To win the main lottery prize, several numbers on the lottery ticket must match the randomly drawn numbers within a certain range during the draw. For example, you need to guess six numbers from 1 to 49 or five numbers from 1 to 36, etc.

Write a function `get_numbers_ticket(min, max, quantity)` that helps generate a set of unique random numbers for such lotteries. It returns a random set of numbers within the given parameters, ensuring all numbers in the set are unique.

#### Task Requirements:
- Function parameters:
  - `min` - the minimum possible number in the set (no less than 1).
  - `max` - the maximum possible number in the set (no more than 1000).
  - `quantity` - the number of numbers to pick (values between `min` and `max`).
- The function generates the specified number of unique numbers within the given range.
- The function returns a list of randomly selected, sorted numbers. The numbers in the set must not repeat. If the parameters do not meet the specified constraints, the function returns an empty list.

#### Recommendations:
1. Ensure that the input parameters meet the specified constraints.
2. Use the `random` module to generate random numbers.
3. Use a set or another mechanism to ensure the uniqueness of numbers.
4. Remember that `get_numbers_ticket` returns a sorted list of unique numbers.

#### Evaluation Criteria:
- Validity of input data: the function should check the correctness of the parameters.
- Uniqueness of results: all numbers in the output should be unique.
- Compliance with requirements: the result should be in the form of a sorted list.
- Code readability: the code should be clean and well-documented.

#### Example:
Suppose you need to choose 6 unique numbers for a lottery ticket where the numbers must be in the range from 1 to 49. You can use your function like this:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)

This code calls the `get_numbers_ticket` function with parameters `min=1`, `max=49`, and `quantity=6`. As a result, you will get a list of 6 random, unique, and sorted numbers, such as [4, 15, 23, 28, 37, 45]. Each time the function is called, you will get a different set of numbers.

### Task 3
In your company, an active marketing campaign is conducted using SMS mailings. For this, you collect customers' phone numbers from the database, but often encounter numbers recorded in different formats. For example:
- "+38(050)123-32-34"
- "0503451234"
- "(050)8889900"
- "38050-111-22-22"
- "38050 111 22 11"

Your mailing service can effectively send messages only when the phone numbers are presented in the correct format. Therefore, you need a function that automatically normalizes phone numbers to the required format by removing all unnecessary characters and adding the country code if necessary.

Develop a function `normalize_phone(phone_number)` that normalizes phone numbers to the standard format, leaving only digits and the '+' symbol at the beginning. The function takes one argument—a string with a phone number in any format and converts it to the standard format, leaving only digits and the '+' symbol. If the number does not contain an international code, the function automatically adds the code '+38' (for Ukraine). This ensures that all numbers are suitable for sending SMS.

#### Task Requirements:
- The parameter `phone_number` is a string with a phone number in various formats.
- The function removes all characters except digits and the '+' symbol.
- If the international code is missing, the function adds the code '+38'. This accounts for cases where the number starts with '380' (only '+' is added) and when the number starts without a code ('+38' is added).
- The function returns the normalized phone number as a string.

#### Recommendations:
1. Use the `re` module for regular expressions to remove unnecessary characters.
2. Check if the number starts with '+', and correct the prefix according to the guidelines.
3. Remove all characters except digits and '+' from the phone number.
4. Don't forget to return the normalized phone number from the function.

#### Evaluation Criteria:
- Function correctness: the function should correctly handle different formats of numbers, considering the presence or absence of an international code.
- Code readability: the code should be clean, well-organized, and well-documented.
- Proper use of regular expressions to remove unnecessary characters and format the number.

#### Example Usage:
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS mailings:", sanitized_numbers)

As a result, you should get a list of phone numbers in the standard format, ready for use in SMS mailings:
Normalized phone numbers for SMS mailings: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']


### Task 4
In your organization, you are responsible for organizing birthday greetings for colleagues. To optimize this process, you need to create a function `get_upcoming_birthdays` that helps you determine which colleagues need to be congratulated. The function should return a list of all colleagues whose birthdays are coming up in the next 7 days, including the current day.

You have a list of `users`, where each element contains information about the user's name and birthday. Since colleagues' birthdays may fall on weekends, your function should also consider this and move the congratulation date to the next working day if necessary.

#### Task Requirements:
- The `users` parameter is a list of dictionaries, where each dictionary contains the keys `name` (the user's name, a string) and `birthday` (the birthday, a string in the format 'year.month.date').
- The function should determine whose birthdays fall in the next 7 days, including the current day. If the birthday falls on a weekend, the congratulation date is moved to the next Monday.
- The function returns a list of dictionaries, where each dictionary contains information about the user (key `name`) and the congratulation date (key `congratulation_date`, data in the format 'year.month.date').

#### Recommendations:
1. Assume you receive a list of `users`, where each dictionary contains `name` (user's name) and `birthday` (birthday date as a string in the format 'year.month.date'). Convert the birthday dates from strings to `datetime` objects - `datetime.strptime(user["birthday"], "%Y.%m.%d").date()`. Since only the date is needed (without time), use `.date()` to get just the date.
2. Determine the current system date using `datetime.today().date()`.
3. Iterate through the list of `users` and analyze the birthdays of each user (`for user in users:`).
4. Check if the birthday has already passed this year (`if birthday_this_year < today`). If so, consider the date for the next year.
5. Determine the difference between the birthday and the current day to identify birthdays in the next week.
6. Check if the birthday falls on a weekend. If so, move the congratulation date to the next Monday.
7. Create a data structure that will store the user's name and the corresponding congratulation date if the birthday occurs within the next week.
8. Output the collected data as a list of dictionaries with the users' names and congratulation dates.

#### Evaluation Criteria:
- Relevance and correctness in identifying birthdays in the next 7 days.
- Correct handling of cases when birthdays fall on weekends.
- Code readability and structure.

 Correct handling of cases when birthdays fall on weekends.
- Code readability and structure.

#### Example:
Suppose you have a list of `users`:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Using the `get_upcoming_birthdays` function:
upcoming_birthdays = get_upcoming_birthdays(users)
print("Birthday congratulations list for this week:", upcoming_birthdays)

If today is January 22, 2024, the result might be:
[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]
This list contains information about who and when to congratulate on their birthday.
