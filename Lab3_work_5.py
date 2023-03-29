# # Task №5. Create a class for working with lines
class MyString(str):

    def __init__(self, value):
        self.value = value

    def append_str(self, add_string):
        """Method similar to the append method in the lists"""
        self.value = f'{self.value} {add_string}'

    def pop_str(self, ind=-1):
        """Method similar to the pop method in the lists"""
        lst = list(self.value.split())
        temp = lst[ind]
        lst.pop(ind)
        self.value = " ".join(lst)
        return temp

    def pop_str_2(self, ind=-1):
        """Method similar to the pop method in the lists"""
        temp = self.value[ind]
        lst = list(self.value)
        lst.pop(ind)
        self.value = "".join(lst)
        return temp

    def __str__(self):
        return self.value


a = MyString("Hello, World!")
print(a)

a.append_str("Hello, python!")
print(a)

print(a.pop_str())
print(a)

print(a.pop_str_2())
print(a)

a.append_str("Home work")
print(a)

