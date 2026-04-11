import json
from rich.pretty import pprint
from collections import defaultdict
import sys
from typing import Callable, Optional
from pathlib import Path
from rich.console import Console
from rich.theme import Theme
from functools import wraps

# ===== GLOBALS =====
INVENTORY_FILE_NAME = 'inventory.json'
custom_theme = Theme({
    "success": "green",
    "error": "red italic",
    "info": "bright_yellow bold",
    "default": "#d0d0d0",
    "dim": "gray23"
})
console = Console(theme=custom_theme)

# ===== HELPERS =====

def log_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print the original function's name
        # console.print(f"🔳 {func.__name__}", style="dim")
        return func(*args, **kwargs)
    return wrapper

@log_name
def print_line(num, char="="):
    print(char*num)

@log_name
def print_error(message):
    print_line(10, '〰')
    console.print(message, style="error")

@log_name
def exit_error():
    console.print("Exiting", style="error")
    print_line(10)
    sys.exit()

@log_name
def view_list(items_list):
    pprint(items_list, expand_all=True)

@log_name
def get_available_actions(actions_map):
    return list(actions_map.keys())

@log_name
def print_menu(menu_items):
    print_line(30)
    for number, action in enumerate(menu_items, 1):
        console.print(f"{number}. {action}", style="default")

@log_name
def get_choice(actions_map: list) -> Optional[int]:
    console.print("Оберіть номер дії: ", style="success")
    choice = input()
    if choice.lower() in ['x', 'q']:
        sys.exit()
    try:
        idx = int(choice)
    except ValueError:
        print_error("Введіть ЧИСЛО ліворуч від вибору")
        return None
    if not 0 < idx <= len(actions_map):
        print_error("Невірне число")
        return None
    return idx

@log_name
def get_file_path(file_name: str) -> Path:
    file_path = Path(__file__).parent / file_name
    if not file_path.exists():
        raise FileNotFoundError
    elif not file_path.is_file():
        raise ValueError(f"Not a file '{file_path}'")
    return file_path

@log_name
def int_keys(obj):
    return {int(k) if k.isdigit() else k: v for k, v in obj.items()}

@log_name
def read_json_file(file_path) -> list|dict:
    with file_path.open(mode="r", encoding="utf-8") as json_file:
        data = json.load(json_file, object_hook=int_keys)
    
    return data

# ===== USER =====
@log_name
def get_user_data() -> dict:
    console.print("Enter user name or press Enter to use `user`: ")

    ok = False
    file_path = Path()

    while not ok:
        user_name = input()
        if user_name == "":
            user_name = "user"
        file_name = f"{user_name}.json"
        try:
            file_path = get_file_path(file_name)
            ok = True
        except ValueError as error:
            print_error("enter name of the FILE\n" + f"{error}")
        except FileNotFoundError:
            print_error("file not found")    
            console.print("Try again", style="info")
            print_line(10)

    data = read_json_file(file_path)
    console.print(data)
    result = data if type(data) is dict else {}    
    return result

user = get_user_data()
user["cart"] = defaultdict(int)

@log_name
def print_user_info(user):
    console.print(f"""
        Ім'я покупця        = {user.get("name", "Guest")}
        Грошей в гаманці    = {user["money_left"]}
    """, style="info")
    console.print("Ваш кошик містить:", style="success")
    for k, v in user["cart"].items():
        console.print(f"{k} ({v} шт.)", style="info")

# ===== GOODS =====

@log_name
def get_inventory_data() -> dict[int, dict]:
    file_name = INVENTORY_FILE_NAME
    file_path = Path()
    try:
        file_path = get_file_path(file_name)
    except ValueError as error:
        print_error("enter name of the FILE\n" + f"{error}")
        exit_error()
    except FileNotFoundError:
        print_error("file not found")
        exit_error()

    data = read_json_file(file_path)
    result = data if type(data) is dict else {}
    # if not data:
    #     data = {}
    return result

inventory = get_inventory_data()

@log_name
def get_inventory(query = "available"):
    if query == "available":
        return { k: v for k, v in inventory.items() if v["in_stock"] > 0}
    elif query == "sold":
        return { k: v for k, v in inventory.items() if v["in_stock"] == 0}

@log_name
def buy(id, user):
    item = inventory[id]

    if item["price"] > user["money_left"]:
        console.print("Недостатньо коштів", style="error")
    else:
        item_name = item["name"]
        user["cart"][item_name] += 1
        user["money_left"] -= item["price"]
        item["in_stock"] -= 1
        print_user_info(user)

@log_name
def inform():
    console.print("Ми повідомимо про наявність", style="info")

goods_actions = {
    "Придбати": buy,
    "Список": view_list,
    "Повідомити про наявність": inform,
    "🔙 Назад": print
}

@log_name
def goods_menu(context, goods, can_buy):
    while True:

        print_menu(context)
        idx = get_choice(context)

        if idx is None:
            continue
        
        if idx == 1:
            if not can_buy:
                inform()
                return
            keys = get_available_actions(goods)
            while True:
                view_list(goods)
                choice = input("Оберіть товар ")
                if choice.lower() in ['x', 'q']:
                    sys.exit()
                try:
                    id = int(choice)
                except ValueError:
                    console.print("Введіть ЧИСЛО ліворуч від вибору", style="error")
                    continue
                if id in keys:
                    buy(id, user)
                    break
                else:
                    console.print(f"Товара з артикулом {id} не знайдено.", style="error")
            
        if idx == 2:
            view_list(goods)
        if idx == 3:
            inform()
        if idx == 4:
            return

# ===== BOOKS =====

books = {
    "complaints": [],
    "proposals": []
}

@log_name
def add_record(book):
    text = input("Введіть скаргу/пропозицію: ")
    book.append(text)

@log_name
def view_book(book):
    view_list(book)

books_actions = {
    "Додати Запис": add_record,
    "Подивитись": view_book,
    "🔙 Назад": print
}

@log_name
def books_menu(context, book):
    while True:
        print_menu(context)
        idx = get_choice(context)

        if idx is None:
            continue

        if idx == 1:
            add_record(book)
        if idx == 2:
            view_book(book)
        if idx == 3:
            return

@log_name
def get_book(type):
    if type not in books:
        return None
    return books[type]

@log_name
def say_goodbye():
    user_name = user.get("name", "Guest")
    return "Goodbye, " + user_name

actions: dict[str, Callable] = {
    "Наявні": get_inventory("available"),
    "Закінчились": get_inventory("sold"),
    "Скарги": get_book("complaints"),
    "Пропозиції": get_book("proposals"),
    "Вихід": say_goodbye()
}

# ========== MAIN ===========

@log_name
def start_shop():
    
    # try:
    #     user_name = user["name"]
    # except KeyError:
    #     user_name = "Guest"

    user_name = user.get("name", "Guest")

    console.print(f"""Привіт [green]{user_name}[/].
            Вітаємо в нашій Фантастичній Крамниці!""", style="info")
    print_line(46)
    main_loop()

@log_name
def main_loop():
    console.print("Для виходу введіть [red]'x'[/] або [red]'q'[/]", style="info")
    while True:
        context = get_available_actions(actions)
        print_menu(context)

        idx = get_choice(context)

        if idx is None:
            continue

        value = list(actions.values())[idx - 1]

        if idx in [1, 2]:
            can_buy = False
            if idx == 1:
                can_buy = True
            goods = value
            context = get_available_actions(goods_actions)
            goods_menu(context, goods, can_buy)
        if idx in [3, 4]:
            book = value
            context = get_available_actions(books_actions)
            books_menu(context, book)
        if idx == 5:
            greeting = value
            print(greeting)
            sys.exit()

if __name__ == "__main__":
    start_shop()
