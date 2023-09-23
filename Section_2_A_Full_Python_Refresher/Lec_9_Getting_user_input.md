## Getting User Input

`input()` function

```python
name = input("Enter your name: ")
print(name)
```

Output

```
Enter your name: Harrison
Harrison
```

## Math on user input

```python
size_input = input("How big is your house (in square feet): ")
square_metres = size_input / 10.8
print(square_metres)
```

Output

```
...
TypeError: unsupported operand type(s) for /: 'str' and 'float'
```

To fix error go to

```python
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(square_metres)
```

### Formating challenge

```python
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres} square metres.")
```

Output

```
How big is your house (in square feet): 500
500 square feet is 46.29629629629629 square metres.
```

little more formatting for the nums after decimal

```python
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")
```

Which changes that line to

```
500 square feet is 46.30 square metres.
```

Link from the instructor: https://blog.teclado.com/python-formatting-numbers-for-printing/
