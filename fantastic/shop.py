from pprint import pprint
from collections import defaultdict
import sys
from typing import Callable


# ===== HELPERS =====

def get_available_actions(actions_map):
    return list(actions_map.keys())

def print_menu(menu_items):
    print( "~"*30)
    for number, action in enumerate(menu_items, 1):
        print(f"{number}. {action}")

def get_choice(actions_map):
    choice = input("Оберіть номер дії: ")
    if choice.lower() in ['x', 'q']:
        sys.exit()
    try:
        idx = int(choice)
    except ValueError:
        print("Enter a NUMBER to the left of your choice")
        return None
    if not 0 < idx <= len(actions_map):
        print("Incorrect number")
        return None
    return idx

# ===== USER =====

user = {
    "name": "Celebrity",
    "cart": defaultdict(int),
    "money_left": 10000
}

def print_user_info(user):
    print(f"""
        Name = {user["name"]}
        Money Left {user["money_left"]}
    """)
    print("Your cart has:")
    for k, v in user["cart"].items():
        print(f"{k} ({v} шт.)")

# ===== GOODS =====

inventory = {
1:{
    "name": "Цвяхи олов'яні",
    "in_stock": 0,
    "price": 1, 
    }, 
2: {
    "name": "Гудзики дерев'яні",
    "in_stock": 5,
    "price": 25, 
    }, 
3: {
    "name": "Парфуми духмяні",
    "in_stock": 10,
    "price": 400, 
    }
}

def get_inventory(query = "available"):
    if query == "available":
        return { k: v for k, v in inventory.items() if v["in_stock"] > 0}  # ty:ignore[unsupported-operator]
    elif query == "sold":
        return { k: v for k, v in inventory.items() if v["in_stock"] == 0}

def buy(id, user):
    item = inventory[id]

    if item["price"] > user["money_left"]:
        print("You don't have enough money")
    else:
        item_name = item["name"]
        user["cart"][item_name] += 1
        user["money_left"] -= item["price"]
        item["in_stock"] -= 1  # ty:ignore[unsupported-operator]
        print_user_info(user)

def inform():
    print("Ми повідомимо про наявність")

goods_actions = {
    "Придбати": buy,
    "Повідомити про наявність": inform,
    "🔙 Назад": print
}

def goods_menu(context, goods, can_buy):
    while True:

        print_menu(context)
        idx = get_choice(context)

        if idx is None:
            continue
        
        if idx == 3:
            return

        if idx == 1:
            if not can_buy:
                inform()
                return
            keys = get_available_actions(goods)
            while True:
                pprint(goods, indent=4)
                choice = input("Оберіть товар ")
                if choice.lower() in ['x', 'q']:
                    sys.exit()
                try:
                    id = int(choice)
                except ValueError:
                    print("Enter a NUMBER to the left of your choice")
                    continue
                if id in keys:
                    buy(id, user)
                    break
                else:
                    print(f"Товара з артикулом {id} не знайдено.")
            
        if idx == 2:
            inform()

# ===== BOOKS =====

books = {
    "complaints": [],
    "proposals": []
}

def add_record(book):
    text = input("Введіть скаргу.пропозицію")
    book.append(text)

def view_book(book):
    print(book)

books_actions = {
    "Додати Запис": add_record,
    "Подивитись": view_book,
    "🔙 Назад": print
}

def books_menu(context, book):
    while True:
        print_menu(context)
        idx = get_choice(context)

        if idx is None:
            continue
        
        if idx == 3:
            return

        if idx == 1:
            add_record(book)
        if idx == 2:
            view_book(book)

def get_book(type):
    if type not in books:
        return None
    return books[type]

def say_goodbye(name: str = "Guest"):
    return "Goodbye, " + name

actions: dict[str, Callable] = {
    "Наявні": get_inventory("available"),
    "Закінчились": get_inventory("sold"),
    "Скарги": get_book("complaints"),
    "Пропозиції": get_book("proposals"),
    "Вихід": say_goodbye()
}

# ========== MAIN ===========

def start_shop():
    print("Hello from Fantastic Shop!")
    main_loop()

def main_loop():
    print("Для виходу введіть 'x' або 'q'")
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
            # print(goods)
            context = get_available_actions(goods_actions)
            goods_menu(context, goods, can_buy)
        if idx in [3, 4]:
            book = value
            # print(book)
            context = get_available_actions(books_actions)
            books_menu(context, book)
        if idx == 5:
            greeting = value
            print(greeting)
            sys.exit()

if __name__ == "__main__":
    start_shop()
