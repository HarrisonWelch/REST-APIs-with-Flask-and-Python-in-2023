# Writing our first Python app

Building our first app. As a recap of everything learned so far.

## App design

Ask user for input and enter how many months that is equal to.

Can put functions inside of functions.

```python
user_age = int(input("Enter your age: "))
months = user_age * 12
print(f"Your age, {user_age}, is equal to {months} months.")
```

Output

```
Enter your age: 26
Your age, 26, is equal to 312 months.
```

## Addition challenge

Print the number of seconds

```python
user_age = int(input("Enter your age: "))
months = user_age * 12

days_in_a_year = 365.2425
hours_in_a_day = 24
mins_in_an_hour = 60
secs_in_a_min = 60

print(
    f"Your age, {user_age}, is equal to {months} months. That is also about {user_age * days_in_a_year * hours_in_a_day * mins_in_an_hour * secs_in_a_min:.2f} seconds.")
```

Output

```
Enter your age: 26
Your age, 26, is equal to 312 months. That is also about 820480752.000
```