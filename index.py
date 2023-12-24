def save():
    name = input("Enter your name: ")
    file = open("db.txt","a")
    file.write(name)
    file.close()

def load():
    name = input("Enter your name: ")
    file = open("db.txt","r")

    lines = file.readlines()
    for i in lines:
        if i == name:
            file.close()
            print("Welcome back " + name)
        else:
            print("I dont know " + name)

while True:
    user_input = input("Are you new(Y/N): ").upper()
    
    if user_input == "Y":
        save()
    else:
        load()

    is_continue = input("Do you want to continue?(Y/N): ").upper()
    if is_continue == "N":
        break
    else:
        pass
