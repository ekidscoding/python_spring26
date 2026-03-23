num1 = 123
print(type(num1).__name__)

str1 = "123"
print(type(str1).__name__)

num2 = 123.456
print(type(num2).__name__)

a = 10
b = 10
my_bool = a == b
print(type(my_bool).__name__)
print(my_bool)

n = None
if n is None:
    print("nothing here")