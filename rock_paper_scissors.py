import random
gamelist={"rock", "paper", "scissors"}
print("Welcome to the Rock, Paper, Scissors game!")
userskor = 0
computerskor = 0

while True:
    user_choice = input("Enter your choice: rock, paper, or scissors: ")
    computer_choice = random.choice(list(gamelist))
    if(user_choice == "exit"):
        if(userskor>computerskor):
            print("user wins and the score is: ", userskor)
        elif(userskor<computerskor):
            print("computer wins and the score is: ", computerskor)
        else:
            print("tie with the score: ", userskor)
        break
    print("Computer choice: ", computer_choice)

    if (user_choice == computer_choice):
        print("The computer chose the same thing. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("user wins")
        userskor += 1
    else:
        print("computer wins")
        computerskor += 1
    


