# Class inheritance

Start here

```py
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")

printer = Device("Printer", "USB")
print(printer)
printer.disconnect()

# > Device 'Printer' (USB)
# > Disconnected
```

Add functionality to print things out like a Printer.

Remember to call `super()`

```py
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity # Max cap
        self.remaining_pages = capacity # Curr cap

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)

# > Printing 20 pages.
# > Device 'Printer' (USB) (480 pages remaining)
```

The superclass is inherited like a parameter on a function `Printer(Device)`

All objects use inherit from the base Object class

And disconnecting will make the printer fail

```py
...
printer.disconnect()
printer.print(30)

# > Disconnected
# > Your printer is not connected!
```
