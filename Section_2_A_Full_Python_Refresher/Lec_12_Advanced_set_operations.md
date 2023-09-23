# Advanced set operations

## Difference

```python
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)
# > {'Rolf'}
```

switching the order will produce a strange effect. Start with Bob and Anne then subtract away Bob, Anne, and Rolf which gives an empty set.

```python
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = abroad.difference(friends)
print(local_friends)
# > set()
```

`set()` is notation for an empty set. And this is how you make one.

## Union (OR)

To combine a list of abroad and local friends

```python
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)
# > {'Bob', 'Rolf', 'Anne'}
```

## Intersection (AND)

To determine what friends take both classes

```python
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)
# > {'Bob', 'Jen'}
```

## Links

Set operators: https://blog.teclado.com/python-set-operators/

Symetric Difference: https://blog.teclado.com/python-symmetric-difference/

Day 11: Sets: https://teclado.com/30-days-of-python/python-30-day-11-sets/
