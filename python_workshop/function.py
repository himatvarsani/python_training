#!/Users/himat.varsani/.pyenv/shims/python

from datetime import datetime

# def is a name of a function - unique
def calculate_age(my_user_year):
    age = datetime.now().year - int(my_user_year)
    return age

date = input("Enter the year you were born? ")
user_age = calculate_age(date)
print(user_age)