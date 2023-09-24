# Dictionary Comprehension

Like list comp but key-value pairs

```py
users = [
    (0, "Bob" , "password"),
    (1, "Rolf" , "bob123"),
    (2, "Jose" , "longp4assword"),
    (3, "username" , "1234")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
# > {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'bob123'), 'Jose': (2, 'Jose', 'longp4assword'), 'username': (3, 'username', '1234')}
```

The value you put into the new dictionary is the entire tuple with a key of the 2nd value, username.

Then you can access the tuple via username.

```py
...
print(username_mapping["Bob"])
# > (0, 'Bob', 'password')
```

The harder way is to do this

```py
for user in users:
    if user[1] == "Bob":
        # Login stuff
        print(user)

# > (0, 'Bob', 'password')
```

## Example login service

```py
users = [
    (0, "Bob" , "password"),
    (1, "Rolf" , "bob123"),
    (2, "Jose" , "longp4assword"),
    (3, "username" , "1234")
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]
# Take the username to select the right tuple, then destruct into the username and password.
# Don't care about the ID so we use underscore

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")
```

Example input/output:

```
Enter your username: Rolf
Enter your password: bob123
Your details are correct!
```
