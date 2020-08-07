try:
    age = int(input("Age: "))
    income = int(input('Income: '))
    risk = income/age
    print(f'Your risk is {risk}')
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Must enter number greater than 0 for "Age"')