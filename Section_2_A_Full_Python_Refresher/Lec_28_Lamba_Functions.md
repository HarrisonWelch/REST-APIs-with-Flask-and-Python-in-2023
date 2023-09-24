# Lamba Functions

Diff type of function that usually does not have a name and can return values.

Designed to op on inputs and return outputs.

Traditional

```py
def add(x, y):
    return x + y

print(add(5,7))
# > 12
```

with lambda

```py
add = lambda x, y: x + y

print(add(5,7))
# > 12
```

lambdas are meant to be short and usually not have a name

You can also use it like this

```py
print((lambda x, y: x + y)(5, 7))
# > 12
```

this creates a nameless function and then immidiately uses it

But this reads terribly and it is not used often at all.

## Map

```py
def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [double(x) for x in sequence]
```

Use map

```py
doubled = map(double, sequence)
```

Pass it the function in the first arg and the array in 2nd.

May want to use map over listComp if you want a similar style with other langs like JS.

```py
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))
```

These are the same. Map returns a map object. Use list() to see the values.

Lambdas are a function without a name. Almost always single line and do one purpose.
