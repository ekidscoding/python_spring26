# Вправа 00, тренувальна
# Напиши програму, яка містить 
# одну функцію із назвою hello_func
# Функція приймає на вході: 
# name:str, times: int (не обов'язково)
# ім'я кого привітати, times - скільки разів
# 
# Приклад 1
# hello_func("Guido", 3) має повернути
# Hello Guido Hello Guido Hello Guido
#
# Приклад 2
# hello_func("World") має повернути
# Hello World

# Пишіть тут ↓

# def hello_func(name, times=1):
#     message = f"Hello {name}"
#     result = message
#     while times > 1
#         result += ' ' + message
#         times -= 1
#     return result

# def hello_func(name, times=1):
#     message = f"Hello {name}"
#     result = message
#     for _ in range(times-1):
#         result += ' ' + message
#     return result

# def hello_func(name, times=1):
#     return ' '.join([f"Hello {name}"] * times)

# from itertools import repeat
# def hello_func(name, times=1):
#     return ' '.join(repeat(f"Hello {name}", times))

# Не чіпайте код під цією рискою
# ------------------------------
print(hello_func("Guido", 3))  # Має надрукувати "Hello Guido Hello Guido Hello Guido"
assert hello_func("Guido", 3) == "Hello Guido Hello Guido Hello Guido"  #, "Виникла помилка при перевірці завдання 1"
print(hello_func("World"))  # має надрукувати "Hello World"
assert hello_func("World") == "Hello World"  #, "Виникла помилка при перевірці завдання 1"