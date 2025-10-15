import random
def get_computer_choice():
    return random .choice(['rock','paper','scissors'])
def determine_winner(player,computer):
    if player==computer:
        return 'tie'
    elif (player=='rock' and computer=='scissors') or \
         (player=='paper' and computer=='rock') or \
         (player=='scissors' and computer=='paper'):
        return 'player'
    else:
        return 'computer'
def play_round(round_number):
    while True:
        player_choice=input(f"Round{round_number} - Choose rock,paper, or scissors:").lower()
        if player_choice in ['rock','paper','scissors']:
            break
        print("Invalid choice. Try again.")
    computer_choice=get_computer_choice()
    print(f"Computer chose:{computer_choice}")    
    winner = determine_winner(player_choice,computer_choice)
    if winner=='player':
        print("you win this round!")
    elif winner=='computer':
        print("computer wins this round!")
    else:
        print("Its a tie!")
    return winner,player_choice,computer_choice
def main():
    print("welcome to Rock-Paper-scissors Game!")       
    while True:
        try:
            total_rounds=int(input("enter number of rounds you want to play:"))      
            if total_rounds>0:
                break
            else:
                print("enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a number.")
    player_score=0
    computer_score=0
    tie_count=0
    history=[]
    for round_number in range(1,total_rounds+1):
        winner,player_choice,computer_choice= play_round(round_number)
        #Update scores
        if winner=='player':
            player_score+=1
        elif winner=='computer':
            computer_score+=1
        else:
            tie_count+=1
        history.append({
            'round':round_number,
            'player':player_choice,
            'computer':computer_choice,
            'winner':winner
        })   
        print(f"Score=>You:{player_score} | Computer: {computer_score} | Ties:{tie_count}\n")
        #Final results
        print("\n---Game Over---")
        print(f"Final Score => You: {player_score} | Computer:{computer_score} | Ties:{tie_count}")
        if player_score > computer_score:
            print("Congratulations! You won the game!")
        elif player_score < computer_score:
            print("Computer won the game! Better luck next time.")
        else:
            print("The game ended in a tie!")
        print("\n---Round History---")
        for r in history:
            print(f"Round{r['round']}: You-{r['player']} | Computer-{r['computer']} | winner:{r['winner']}")
        #Replay option
        replay=input("\nDo you want to play again?(yes/no):").lower()
        if replay=="yes":
            main()
        else:
            print("Thanks for playing! Goodbye.")
if __name__=="__main__":
    main()                

