# Variables in Python

Link given: https://blog.teclado.com/how-to-set-up-visual-studio-code-for-python-development/

Variables are similar to those in Algebra

Integer

```python
x = 15
```

Float

```python
price = 9.99
```

Math:

```python
discount = 0.2

result = price * (1 - discount)
```

Print:

```python
print(result)
```

Note: Parenthesis earlier was for math order of ops. Here it was used for a function.

This is how you output to the user

Output:

```sh
python .\code.py
7.992000000000001
```

## Strings

Ints and floats are for numbers and math.

Strings are for groups of characters.

```python
name = "Rolf"

print(name)
```

Output

```
Rolf
```

Python uses double and single quotes so long as you don't mix and match. Stick to one type and instructor uses double

What if we use the multiplication operator on a string

```python
print(name * 2)
```

Output

```
RolfRolf
```

What has happened here is automatic concatination. Same as `name + name`

## Changing Variable values

Python creates small variables as soon as it starts up

a has the value of 25 and b is assigned to a

```python
a = 25
b = a
```

We can print those off with print

```python
print(a)
print(b)
```

Output

```
25
25
```

What happens when we change b to 17

```python
a = 25
b = a

b = 17

print(a)
print(b)
```

Output

```
25
17
```

b = 17 is telling python to make 17 and assign it to b, it does not care about it being assigned to a before.
