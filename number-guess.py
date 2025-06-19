import random
from colorama import Fore, Style, init

def play_num_guess():
# Generate a random integer between 1 and 50
    
    yourname =input(Fore.MAGENTA+"Hi! What's your name? ").upper()
    print(Fore.CYAN+f"\nWelcome to this number guessing game {yourname}")
    
    print(Fore.YELLOW+"--------------------------------------------------------------------------------------------")
    print(Fore.BLUE+"Instructions:")
    print(Fore.YELLOW+"A random number will be generated based on the difficulty level and you have to guess the number in minimum attempts")
    print(Fore.YELLOW+"You will only get 10 attempts to get it right")
    print(Fore.YELLOW+"--------------------------------------------------------------------------------------------")
    print(Fore.BLUE+"So, let's get started")
    
    diff= input(Fore.MAGENTA+"Choose difficulty easy/medium/hard ").lower()

    if diff =="easy":
        num = random.randint(1, 20)
        max_attempts=10
        print("You have to guess between 1 and 20")
    elif diff =="medium":
        num = random.randint(1, 50)
        max_attempts=8  
        print("You have to guess between 1 and 50")
    elif diff =="hard":
        num = random.randint(1, 100)
        max_attempts=5
        print("You have to guess between 1 and 100")
      
    
    guesses=0  


    while True:
        guess =int(input(Fore.MAGENTA+"Guess the number : "))
        guesses+=1
        if guess==num: 
            if diff=="easy":
                print(Fore.GREEN+"Yayy! You guessed that right")  
            elif diff=="medium":
                print(Fore.GREEN+"You're smart, that's right")    
            else:
                print("You're a Genius, That's the right answer")    
            print(Fore.GREEN+f"You guessed the number right in {guesses} attempts")     
            break
        elif guesses==max_attempts:
            print(Fore.RED+"Sorry all your attempts are finished, you lost")
            break
        elif guess>num:
           print(Fore.RED+"Try a smaller number")
        elif guess<num:
           print(Fore.RED+"Try a larger number")
        
        
             


while True:
    play_num_guess()
    replay= input(Fore.CYAN+"Do you wanna play again? yes/no : ").lower()
    if replay =="no":
        print(Fore.MAGENTA+"Thank you")
        break