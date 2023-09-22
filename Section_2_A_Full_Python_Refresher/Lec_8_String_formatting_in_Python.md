# String formatting in Python

--- Python 3.6 or later

```python
name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)
```

Output

```
Hello, Bob
Hello, Bob
```

You would have to change greeting as it's not dynamic

Put an f in front of the string.

```python
greeting = f"Hello, Bob"
```

Then we can use curly braces to fill in the value

```python
name = "Bob"
greeting = f"Hello, {name}"

print(greeting)
```

Output

```
Hello, Bob
```

Exactly as before

Now if we put back the name re-assign it does not change the problem.

```python
name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name = "Rolf"

print(greeting)
```

Output

```
Hello, Bob
Hello, Bob
```

What you can do is make the f-string in the print func call

```python
name = "Bob"

print(f"Hello, {name}")

name = "Rolf"

print(f"Hello, {name}")
```

Output

```
Hello, Bob
Hello, Rolf
```

## Template Strings

```python
name = "Bob"
greeting = "Hello, {}" # Note: no "f" in front
with_name = greeting.format(name)

print(with_name)
```

Output

```
Hello, Bob
```

Benefit is re-using this template like so:

```python
name = "Bob"
greeting = "Hello, {}" # Note: no "f" in front
with_name = greeting.format("Rolf")

print(with_name)
```

Output

```
Hello, Rolf
```

So it allowes template definition.

```python
name = "Bob"
greeting = "Hello, {}" # Note: no "f" in front
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)
```

Output

```
Hello, Bob
Hello, Rolf
```

format() can be useful over f-strings, but generally f-strings are preferred on 3.6 and later.

Can be used for much longer templates as well

```python
longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)
```

Output

```
Hello, Rolf. Today is Monday.
```
