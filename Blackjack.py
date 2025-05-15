import random

def deal_card():
    '''Reterns a random card'''
    cards = [11, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 10, 10, 10]
    c = random.choice(cards)
    return c

def scor(player):
    if sum(player)==21 and len(player)==2:
        return 0
    if 11 in player and sum(player)> 21:
        player.remove(11)
        player.append(1)
    s = 0
    for i in player:
        s += i 
    return s

def compare(user_scor, computer_scor):
    if user_scor > 21:
        return "You went over, you lose"
    elif user_scor == computer_scor:
        return "Draw"
    elif computer_scor > 21: 
        return "Computer went over, You win"
    elif user_scor > computer_scor:
        return "You win"
    else:
        return "You lose"

'''main'''
def play_game():

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """
    print(logo)
    player = []
    computer = []
    is_game_over = False

    for i in range(2):
        player.append(deal_card())
        computer.append(deal_card())


    while not is_game_over:
        user_scor = scor(player)
        computer_scor = scor(computer)


        print(f"Your cards : {player}, current scor: {user_scor}")
        print(f"Computer's first card: {computer[0]}")

        if user_scor == 0 or computer_scor == 0 or user_scor > 21:
            is_game_over = True
            print("You lose ! ")        
        else:
            user_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            if user_deal == 'y':
                player.append(deal_card())
            else:
                is_game_over = True

    while computer_scor != 0 and computer_scor < 17:
        computer.append(deal_card())
        computer_scor = scor(computer)

    print(f"Your cards are {player} and score is {user_scor}")
    print(f"Computers cards are {computer} and score is {computer_scor}")
    print(compare(user_scor, computer_scor))


while input("Do u want to play Blackjacks. Type Y/N ").lower() == 'y':
    play_game()
