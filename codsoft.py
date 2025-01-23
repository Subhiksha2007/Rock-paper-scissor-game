import random
option=["rock","paper","scissor"]
user=0
computer=0
while   True:
#User's choice
    user_choice=input("Enter (rock/paper/scissor) : ").lower()
#Input validation
    if user_choice not in option:
        print("Invalid choice")
        continue
#Computer's choice 
    computer_choice=random.choice(option)
    print(f"Computer choice is : {computer_choice}")
#Determine the winner and update score
    if (user_choice==computer_choice):
        print("\tMatch Draw")
    elif (user_choice=="rock" and computer_choice=="scissor"):
          print("\tHurray! Yow won the match")
          user+=1
    elif (user_choice=="scissor" and computer_choice=="paper"):
        print("\tHurray! You won the match")
        user+=1
    elif(user_choice=="paper" and computer_choice=="rock"):
        print("\tHurray! You won the match")
        user+=1
    else:
        print("\tOops! You lose the match")
        computer+=1
#Display Scoreboard
    print(f"Scoreboard:\nYou - {user}\nComputer - {computer}")
#Play again or quit condition 
    user_wish=input("Do you want to quit or play again? : ")
    if user_wish=="quit":
        print("\t\tTotal Scores : ")
        print(f"\tYou - {user}\t\t Computer - {computer}")
        print("Bye! See you soon")
        break
