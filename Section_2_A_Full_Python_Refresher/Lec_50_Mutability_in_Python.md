# Mutability in Python

```py
a = []
b = a

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))

```

Out

```
[35]
[35]
1840591229952
1840591229952
```

But change b to its own empty list

```py
a = []
b = []

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))
```

A list is mutable

They are immutable

All things are mutable unless we have no way to change it like Tuple. The error of can't do that will happen before we see a mutable problem.

----

Integers are immutable

Most things are mutable except:
* Tuples
* Integers
* Strings
* Floats
* Booleans

----

```py
a = "Hello"
b = a

print(id(a))
print(id(b))

a += "world"
print(id(a))
print(id(b))

```

This will change a to a new string  but b will retain its memory
