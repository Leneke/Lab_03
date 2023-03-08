class MyString(str):

    def __init__(self, value):
        self.value = value

    def append_str(self, add_string):
        self.value = f'{self.value} {add_string}'


    def pop_str(self, ind):
        lst = list(self.value.split())
        temp = lst[ind]
        lst.pop(ind)
        self.value = " ".join(lst)
        return temp

    def pop_str_2(self, ind):
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

print(a.pop_str(-1))
print(a)

print(a.pop_str_2(-1))
print(a)

a.append_str("Home work")
print(a)


