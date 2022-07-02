import random

def rules():
    gameRule = "Game rules \n Only input from available options - \n \
r - Rock \n p - Paper \n s - Scissor \n q - quit the game \n rules - Display game rules"
    return gameRule

def play():
    user = input("Choose your hand:\n'r': rock, 'p': paper, 's': scissor \n")
    while inputCheck(user) != True:
        user = input("=======================\nChoose available hand: r, s, p \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return '=======================\n You draw! Try again?\n======================='
    #put win condition
    elif is_win(user, computer):
        return '=======================\n You won dude!\n======================='
    elif is_win(computer, user):
        return '=======================\n You lost!\n======================='
    
    return

#Check user input validity
def inputCheck(userTyped):
    
    validInput = 'rps'
    if userTyped == 'q':
        return quit()
    elif userTyped == 'rules':
        print(rules())
        return
    elif userTyped not in validInput:
        return False 
    return True

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(rules())
while True:
    print(play())
