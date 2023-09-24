# Functions

Name code and reuse it

When python hits a `def` keyword

```python
def hello():
    print("Hello!")
```

This defines but does not run

```python
def hello():
    print("Hello!")

hello()
```

Output

```
Hello!
```

Indentation is important again here

```py
print("Welcome to the age in seconds program!")

def user_age_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")

user_age_seconds()

print("Goodbye!")
```

Output Example:

```
Welcome to the age in seconds program!
Enter your age: 27
Your age in seconds is 851472000
Goodbye!
```

## Shadowing

This can be a problem when you define your own stuff over python's built-ins

```python
def print():
    print("Hello, World!")

print()
# > TypeError: print() takes 0 positional arguments but 1 was given
```

## Scoping

```python
friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name:")
    friends = friends + [friend_name]

add_friend()
# > UnboundLocalError: cannot access local variable 'friends' where it is not associated with a value
```

friends in the global scope of the file and friends in the function scope.

## Use before assignment

```py
say_hello()

def say_hello():
    print("Hello!")

# > NameError: name 'say_hello' is not defined
```

## Strange ordering

```py
def add_friend():
    friends.append("Rolf")

friends = []
add_friend()

print(friends)
# > ['Rolf']
```

friends is defined when the function is called but it is very weird to read.
