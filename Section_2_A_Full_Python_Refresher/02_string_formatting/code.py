# name = "Bob"

# print(f"Hello, {name}")

# name = "Rolf"

# print(f"Hello, {name}")

# ----

# name = "Bob"
# greeting = "Hello, {}" # Note: no "f" in front
# with_name = greeting.format(name)
# with_name_two = greeting.format("Rolf")

# print(with_name)
# > Hello, Bob
# print(with_name_two)
# > Hello, Rolf

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)
