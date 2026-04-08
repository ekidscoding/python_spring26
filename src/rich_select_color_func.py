from rich.pretty import pprint
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "success": "green",
    "error": "red italic",
    "info": "bright_yellow bold"
})

console = Console(theme=custom_theme)

styles = {
    "1": "red italic",
    "2": "green bold",
    "3": "gold3 on royal_blue1",
    "4": "#af00ff",
    "5": "rgb(175,0,255)",
    "6": "cyan strike",
    "7": "yellow on blue"
    }

def get_colored_message(styles=styles):
    styles_len = len(styles.items())
    while (user_input := input(f'Набери число від 1 до {styles_len}: ')).lower() not in ['x', 'q']:
        if user_input not in styles:
            console.print("Помилковий ввід", style="error")
            return ""
        c = styles[user_input]
        return f"[{c}]Секретне барвисте повідомлення задане в функції[/]"
    return f"Ви ввели '{user_input}'"


if __name__ == '__main__':
    console.print("Для виходу наберіть [red bold]'X'[/] або [red dim]'Q'[/] (одна літера)", style="info")
    pprint(styles, expand_all=True)
    while (user_input := input("\tПродовжити? Y/n: ")).lower() not in ['n', 'x', 'q']:
        console.print("Зараз обери стиль", style="info")
        console.print(get_colored_message())
    console.print("Дякую за користування програмою", style="success")
