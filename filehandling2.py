try:
    with open("config.txt", "r") as file:
        name = file.read()
        print("Welcome ", name)
except FileNotFoundError:
    with open("config.txt", "w") as file:
        file.write("Saraa")
    with open("config.txt", "r") as file:
        name = file.read()
        print("Welcome", name)
