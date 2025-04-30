import random
input_choice=["rocks","paper","scissors"]
user_wins=0
num = int(input("Enter a number to paly n numbers of times: "))
counter=0
computer_wins=0
while counter < num:
    user_input=input("please enter a user input: ")
    if user_input=="q":
        print("you are out of from the game")
        break
    if user_input not in input_choice:
        continue
    
    com_num=random.randint(0,2)
    computer_guess=input_choice[com_num]
    
    if user_input=="rocks" and computer_guess=="scissors":
        user_wins+=1
        print("you won")
    elif user_input=="scissors" and computer_guess =="rocks":
        print("computer won ")
        computer_wins +=1
    
        
    elif user_input=="paper" and computer_guess=="rocks":
        user_wins +=1
        print("you win")

    elif user_input =="rocks" and computer_guess=="paper":
        computer_wins +=1
        print("computer won ")
        
    elif user_input=="scissors" and computer_guess=="paper":
        user_wins +=1
        print("you win")
    counter +=1
        
    
print("Good bye")
print(user_wins)
print(computer_wins)
        
