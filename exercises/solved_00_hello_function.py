# Вправа 00, тренувальна
# Напиши програму, яка містить 
# одну функцію із назвою hello_func
# Функція приймає на вході: 
# name:str, times: int (не обов'язково)
# ім'я кого привітати, times - скільки разів
# 
# Приклад 1
# hello_func("Guido", 3) має повернути
# Hello Guido|Hello Guido|Hello Guido
#
# Приклад 2
# hello_func("World") має повернути
# Hello World

from rich.console import Console
from rich.theme import Theme

# ===== GLOBALS =====
custom_theme = Theme({
    "success": "green",
    "error": "red italic",
    "default": "#d0d0d0"
})
console = Console(theme=custom_theme)

# Пишіть тут ↓

# def hello_func(name, times=1):
#     prefix = 'Hello '
#     message = prefix + name
#     result = message

#     separator = '|'
#     while times > 1:
#         result += separator + message
#         times -= 1
#     return result

# def hello_func(name, times=1):
#     prefix = 'Hello '
#     message = prefix + name
#     result = message

#     separator = '|'
#     for _ in range(times-1):
#         result += separator + message
#     return result

def hello_func(name, times=1):
    return '|'.join([f"Hello {name}"] * times)

# from itertools import repeat
# def hello_func(name, times=1):
#     return '|'.join(repeat(f"Hello {name}", times))

# Не чіпайте код під цією рискою
# ------------------------------

test_cases = (
   {"args": ("Guido", 3),
   "result": "Hello Guido|Hello Guido|Hello Guido"},
   {"args": ("World",),
   "result": "Hello World"},
   {"args": ("",),
   "result": "Hello "},
)

for num, tc in enumerate(test_cases, start=1):
    args = tc["args"]
    got = hello_func(*args)
    want = tc["result"]
    # assert got == want, f"'{got}' is not equal to '{want}'"
    if got != want:
        console.print(f"'{got}' is not equal to '{want}'", style="error")
    else:
        console.print(f"TEST {num} PASSED {got=} {want=}", style="success")
