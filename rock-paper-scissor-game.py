import random
import sys

def game(name, ch):
    u_score = 0
    c_score = 0
    chances = int(input("\nEnter the number of chances: "))

    while chances>0:
        user = input(f"\n{name}, Enter your choice: ")
        comp = random.choice(ch)
        if user in ch:
            print(f"Computer has selected {comp}")
            if user == 'paper':
                if comp == 'rock':
                    u_score += 1
                elif comp == 'scissor':
                    c_score += 1

            if user == 'rock':
                if comp == 'scissor':
                    u_score += 1
                elif comp == 'paper':
                    c_score += 1

            if user == 'scissor':
                if comp == 'paper':
                    u_score += 1
                elif comp == 'rock':
                    c_score += 1
            
            print(f"{name}'s score is {u_score}")
            print(f"Computer's score is {c_score}")
        
        else:
            print("Choices should be in Format of 'rock','paper','scissor'")
            chances += 1 
        chances -= 1

    if u_score > c_score:
        print(f"Congratulations {name}! You are winner.")

    elif c_score > u_score:
        print(f"Sorry {name}! You lose this game, Computer is winner.")

    else:
        print(f"Game is Tied")

    c = input(f"\n{name}, Do you want to play again Y/N: ")
    if c == 'y' or c=='Y':
        game(name, ch)
    else:
        sys.exit()

if __name__ == "__main__":
    ch = ['rock','paper','scissor']
    print("Choices should be in Format of 'rock','paper','scissor'\n")
    name = input("Enter your name: ")
    game(name, ch)
