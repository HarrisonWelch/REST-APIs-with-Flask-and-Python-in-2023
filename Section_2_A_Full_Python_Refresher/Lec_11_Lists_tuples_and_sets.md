# Lists, tuples, and sets.

List is defined with square brackets `[]`

```python
l = ["Bob", "Rolf", "Anne"]
```

Tuple is with parenthesis `()`

```python
t = ("Bob", "Rolf", "Anne")
```

Set is with curly braces `{}`

```python
s = {"Bob", "Rolf", "Anne"}
```

sets don't need to guarantee order

## Access

Subscript notation

```python
print(l[0])
```

Elements in programming ususally start with zero.

Tuples also work with subscript

```python
print(t[0])
```

But with sets you can't guarantee order. so this would not make much sense and errors out.

```python
print(s[0])
# > TypeError: 'set' object is not subscriptable
```

## Change an array

Simple as `x[y] = z` where x is the array name, y is the index starting with 0 and z is the value to be used to set againt

```python
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

l[0] = "Smith"
print(l[0])
```

Output

```
Smith
```

This does not work with tuple b/c they are not mutable

```python
t = ("Bob", "Rolf", "Anne")

t[0] = "Smith"
# > TypeError: 'tuple' object does not support item assignment
print(t[0])
```

And set does not makes sense b/c order is not controlled. You will get an error similar to the above.

## Adding to list

`append()` - function

```python
l = ["Bob", "Rolf", "Anne"]

l.append("Smith")
print(l)
# > ['Bob', 'Rolf', 'Anne', 'Smith']
```

For tuples this does not work. Append does not exist on the tuple.

```python
t = ("Bob", "Rolf", "Anne")

t.append("Smith")
# > AttributeError: 'tuple' object has no attribute 'append'
print(t)
```

Can't add or remove from tuples

## Removal

```python
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

l.remove("Bob")
print(l)
# > ['Rolf', 'Anne']
```

## Add things to a set

Note that this is `add` not `append` because append means to add to the end but since sets don't have order we can't add specifically to the end.

```python
s = {"Bob", "Rolf", "Anne"}

s.add("smith")
print(s)
# > {'Bob', 'Smith', 'Rolf', 'Anne'}
```

Re-running the same program will result in a diff order.

Also not that sets can't have duplicates so adding "Smith" twice will have no effect.

```python

s.add("Smith")
s.add("Smith")
print(s)
# > {'Anne', 'Smith', 'Bob', 'Rolf'}
```

