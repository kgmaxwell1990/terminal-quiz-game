def show_menu():
    print("1. Ask questions")
    print("2. Add a questions")
    print("3. Exit")
    
    option = input("Enter your choice: ")
    return int(option)

def ask_questions():
    print("You want to ask questions")
    with open("questions.txt") as f:
        lines = f.read().split("\n")
        
    numbered_lines = list(enumerate(lines))
    
    questions = []
    answers = []
    
    for n,t in numbered_lines:
        if n%2 == 0 :
            questions.append(t)
        else:
            answers.append(t)
        
    q_and_a = list(zip(questions, answers))
    
    for q,a in q_and_a:
        guess = input(q)
        if guess == a:
            print("Correct!")
        else:
            print("WRONG!")
    
def add_question():
    print("You want to add a question")
    question = input("Enter a question: ")
    answer = input("Enter the answer: ")
    
    with open("questions.txt", "a") as f:
        f.write(question + "\n")
        f.write(answer + "\n")

    

def game_loop():
    while True:
        option = show_menu()
        
        if option == 1:
            ask_questions()
        if option == 2:
            add_question()
        if option == 3:
            break
        
game_loop()



