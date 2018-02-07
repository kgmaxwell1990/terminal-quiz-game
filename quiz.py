def show_menu():
    print("1. Ask questions")
    print("2. Add a questions")
    print("3. Exit")
    
    option = input("Enter your choice: ")
    return int(option)
    
def game_loop():
    while True:
        option = show_menu()
        
        if option == 1:
            print("You want to ask the questions")
        if option == 2:
            print("You want to add a question")
        if option == 3:
            break
        
game_loop()



# with open("questions.txt") as f:
#     lines = f.read()

# print(lines)