import random,time
def user_guessing_num(level,user_num):
    if level=="HARD" or level=="hard":
        attempt = 5
    else:
        attempt= 10
    guess_num = random.randint(1,100)
    
    game_end = False
    count =0
    while not game_end:
        if user_num == guess_num:
            print(f"you are win the game in {count+1} attempt",end="\n")
            game_end = True
            return True
            
        elif  guess_num > user_num:
            print("Too low",end="\n")
            print(f" you have {attempt-1} remain",end="\n")
            
            attempt -=1
            count +=1
            
        elif guess_num<user_num:
            print("too high",end="\n")
            attempt -=1
            count +=1
        if attempt==0:
            print("you wii lose your game",end="\n")
            game_end  = True
            return False
        user_num= int(input("guess agin: "))
print("Welcome to number guessing game!",end="\n")
level = input("Enter a level: ")
time.sleep(2)
user_num = int(input("ENTER The number: "))
time.sleep(2)
user_guessing_num(level,user_num)