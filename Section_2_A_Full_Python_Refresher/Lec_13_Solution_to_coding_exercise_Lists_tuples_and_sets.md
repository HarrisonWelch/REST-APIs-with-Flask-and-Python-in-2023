# Solution to coding exercise 2 Lists tuples and sets

1. Create list, `my_list`, of 3 numbers that add up to 100\
2. Create tuple, called `my_tuple`, with a single value in it
3. Change `set2` such that `set1.intersection(set2)` returns `{5, 77, 9, 12}`

For part 2, Tuple trips up a lot of people. `(15)` is not a tuple. Usually this is for maths. Add a comma to distiguish it `(15,)`.

For part 3, change set2 to just have the values in it 5, 77, 9, and 12

## Instructor answer

```python
# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [100, 0, 0]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (15,)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

```
