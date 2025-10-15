import random
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_winner(player,computer):
    if player == computer:
        return 'tie'
    elif (player=='rock' and computer=='scissors') or \
         (player=='paper' and computer=='rock') or \
         (player=='scissors' and computer=='paper'):
        return 'player'
    else:
        return 'computer'
def main():
    player_score=0
    computer_score=0
    print("welcome to Rock-Paper-Scissors with Scores!") 
    print("enter 'quit' to exit the game.\n")   
    while True:
        player_choice=input("Choose rock,paper,or scissors:").lower()
        if player_choice=='quit':
            break
        if player_choice not in['rock','paper','scissors']:
            print("Invalid choice. Try again")
            continue
        computer_choice=get_computer_choice()
        print(f"computer chose:{computer_choice}")
        winner=determine_winner(player_choice,computer_choice)
        if winner=='player':
            player_score+=1
            print("you win this round!")
        elif winner=='computer':
            computer_score+=1
            print("computer wins this round!")  
        else:
            print("Its a tie!")      
        print(f"score=> You:{player_score} | computer:{computer_score}\n")
    print("\nFinal Score:")        
    print(f"you:{player_score} | computer:{computer_score}\n")
    if player_score > computer_score:
        print("congratulations! you won the game!")
    elif player_score < computer_score:
        print("computer won the game! Better luck next time.")
    else:
        print("the game ended in a tie!")        
if __name__=="__main__":
    main()

