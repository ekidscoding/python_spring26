names_and_ages = [("John", 45), ("Jane", 42), ("Ben", 30), ("Betty", 19)]

color_preference = []

def get_color(name):
    message = f"Hello {name}! What color do you like?"
    result = input(message)
    return result

def main():
    length = len(names_and_ages)

    for i in range(length):
        name, age = names_and_ages[i]
        color = get_color(name)
        my_dict = {"name": name, "age": age, "color": color}
        color_preference.append(my_dict)

    print(*color_preference, sep='\n')

if __name__ == "__main__":
    main()
