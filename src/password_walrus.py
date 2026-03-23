secret_symbol = ["@", "#", "%"]
secret_db = {"Daryna": "123456789@", "Kyrylo": "987654321#"}

def get_login():
    return input("Будь ласка, введіть Ваш логін: ")

def db_lookup_login(login):
    return login in secret_db
    
def get_password():
    return input("Будь ласка, введіть Ваш пароль: ")

def db_check_password_match(login, password):
    users_pw = secret_db[login]
    umova: bool = users_pw == password
    if umova:
        return True
    else:
        return False

while (login := get_login()) == '' or not db_lookup_login(login):
        print('Вказаний логін не знайдений')

while (pw := get_password()) == '' or not db_check_password_match(login, pw):
        print('Вказана комбінація пароля та логіну не знайдена')

print('Welcome')
