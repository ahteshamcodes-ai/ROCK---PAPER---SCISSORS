import random
choices = ["rock","paper","scissors"]
user_score = 0
computer_score = 0
round = 1
print("***ROCK PAPER SCISSORS GAME***")
print(" BEST OF FIVE ")
print("FIRST TO WIN 3 ROUNDS TO WIN THE GAME")
while user_score < 3 and computer_score <3:
    print(f"\n---Round Number{round}---")
    user = input("Rock,Paper,Scissors:").lower()
    if user not in choices:
        print("Invalid choice , Try again!!!")
        continue
    computer = random.choice(choices)
    print("your score",user)
    print("computer score",computer)
    if user == computer:
        print("Its a tie !!")
    elif((user=="rock" and computer =="scissors")or(user == "paper" and computer=="rock")or(user== "scissors" and computer=="paper")):
        print("You Win !!")
        user_score +=1
    else:
        print("Computer Wins!!")
        computer_score +=1
        print(f"Score: You {user_score} - {computer_score} computer")
        round +=1
    print("\n ==== THE FINAL RESULT====")
    if user_score == 3:
        print("You won the game !!")
    else:
        print("Computer won the game , Better luck next time!!")
    print(f"Final score: You {user_score} - {computer_score} computer")