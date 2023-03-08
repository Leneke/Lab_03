class MyString(str):

    def __init__(self, value):
        self.value = value

    def append_str(self, add_string):
        self.value = f'{self.value} {add_string}'

    def pop_str(self, ind=-1):
        lst = list(self.value.split())
        temp = lst[ind]
        lst.pop(ind)
        self.value = " ".join(lst)
        return temp

    def pop_str_2(self, ind=-1):
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


