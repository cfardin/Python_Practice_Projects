import random

def game(life, guess_num):
    user_guess = 0
    while user_guess != guess_num:
        print(f"You have {life} attemps to guess the number.")
        user_guess = int(input("Make a guess: ")) #user input 
        if user_guess == guess_num:
            print("You have guessed the right number, you win")
        elif user_guess > guess_num:
            life -= 1
            print("Too high!")
            print(f"You have {life} attemps left")
        elif user_guess < guess_num:
            life -= 1
            print("Too low!")
            print(f"You have {life} attemps left")
            

guess_num = random.randint(1, 100) # the random number
print("I am guessing a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

life = 0
if level[0]== 'e':
    life = 10
    game(life, guess_num)
elif level[0] == 'h':
    life = 5
    game(life, guess_num)
else:
    print("error, entered wrong word")
    


    
