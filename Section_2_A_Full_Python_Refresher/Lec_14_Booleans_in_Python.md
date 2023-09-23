# Booleans in Python

Value that can be either true or false. Use that to make decisions.

If a character in a game pressed the up arrow.

`==` to compare to things for equality.

```python
print(5 == 5)
# > True
```

Similarly we have `>`

```python
print(5 > 5)
# > False
```

## Not equal, isDifferent
```python
print(10 != 10)
# > False
```

Comparisons: `==`, `!=`, `>`, `<`, `>=`, `<=`

These behave differently depending on what types of objects you use them on.

## List comparisons

```python
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print (friends == abroad)
# > True
print (friends is abroad)
# > False
```

That is because Python makes memory for each list. Then it does the same with the second list. `is` checks for exactly the same thing whereas == checks for effective equality because they have the same elements spelt the same way. Recommend to always use `==` over `is`
