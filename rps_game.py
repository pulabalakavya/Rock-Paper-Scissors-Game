import random
choices = {
    "rock": "\U0000270A",
    "paper": "\U0000270B",
    "scissors":"\U0000270C"
}
options=list(choices.keys())
print("Welcome to Rock-Paper-Scissors Game!")
print("Type 'rock','paper',or 'scissors' . Type 'quit' to exit.")

while True:
    user_input=input("Your choice:").lower()

    if user_input=="quit":
        print("Thanks for playing!!")
        break
    if user_input not in options:
        print("Invalid choice, try again.")
        continue
    computer_choice=random.choice(options)
    print(f"you chose:{choices[user_input]}")
    print(f"Computer chose:{choices[computer_choice]}")

    if user_input==computer_choice:
        print("Its a tie!\n")   
    elif((user_input=="rock" and computer_choice=="scissors") or 
    (user_input=="paper" and computer_choice=="rock") or 
    (user_input=="scissors" and computer_choice=="paper")):
        print("You win! \n")  
    else:
        print("computer wins!\n")      