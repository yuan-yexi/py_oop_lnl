from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)

# TODO: attempt to change the value of ImmutableClass obj
# obj.value1 = "Hello World"
# print(obj.value1)

# TODO: even class methods cannot change the value
obj.some_func(20)
