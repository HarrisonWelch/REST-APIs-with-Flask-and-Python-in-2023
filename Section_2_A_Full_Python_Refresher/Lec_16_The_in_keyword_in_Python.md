# The in keyword in Python

Check for membership

```py
friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)
# > True
```

Can also do in detection for sets

```py
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

print(user_movie in movies_watched)
```

Output

```
Enter something you've watched recently: The Matrix
True
...
Enter something you've watched recently: Avatar
False
```

Also note you can do string within a string comparison.

```py
a = "abc"
b = "abcdef"

print(a in b)
# > True
```
