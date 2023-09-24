# a = []
# b = []

# a.append(35)

# print(a)
# print(b)

# print(id(a))
# print(id(b))

a = "Hello"
b = a

print(id(a))
print(id(b))

a += "world"
print(id(a))
print(id(b))
