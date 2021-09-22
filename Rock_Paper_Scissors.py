import random
def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()
    
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return "you and the computer have both chosen {}.it's a tie.".format(computer)
    if is_win(user,computer):
        return "you have chosen {} and the computer has chosen {}.You won!".format(user,computer)
    return "you have chosen {} and the computer has chosen {}.You lost!".format(user,computer)
def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False
if __name__ == '__main__':
    print(play())