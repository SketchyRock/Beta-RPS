import random

RPS_tuple = ("rock", "paper", "scizzors")
win = 0
loss = 0 

        
def print_win_loss():
    print(f"Wins: {win}")
    print(f"Losses: {loss}")
    print()

def check_loop(choice1: str, choice2:str):
    global win
    global loss

    if choice1 == choice2:
        print("TIE")
        print_win_loss()
        
    elif (choice1 == "rock") and (choice2 == "paper"):
        print("LOSS")
        loss += 1
        print_win_loss()
        
    elif (choice1 == "rock") and (choice2 == "scizzors"):
        print("WIN")
        win += 1
        print_win_loss()
        
    elif (choice1 == "paper") and (choice2 == "rock"):
        print("WIN")
        win += 1
        print_win_loss()
        
    elif (choice1 == "paper") and (choice2 == "scizzors"):
        print("LOSS")
        loss += 1
        print_win_loss()
        
    elif (choice1 == "scizzors") and (choice2 == "rock"):
        print("LOSS")
        loss += 1
        print_win_loss()
        
    elif (choice1 == "scizzors") and (choice2 == "paper"):    
        print("WIN")
        win += 1
        print_win_loss()

def print_options():
    print("CHOOSE: ")
    print("- Rock")
    print("- Paper")
    print("- Scizzors")
    print("- Exit")
    print()

def game_loop():
    while True:
        print_options()
    
        try:
            user_input = input("You: ").lower()
            if user_input == "exit":
                break
            random_RPS = random.choice(RPS_tuple)
            print(f"Enemy: {random_RPS}")
            
            check_loop(user_input, random_RPS)
            
        except TypeError:
            print("TypeError: Improper Input")


def simulated_iterations(iterations: int):
    for i in range(iterations):
            user_input = random.choice(RPS_tuple)
            random_RPS = random.choice(RPS_tuple)
            
            check_loop(user_input, random_RPS)

            print("\n--FINAL RESULTS--\n")
            print_win_loss()

def print_title():
    print("Welcome to - Rock Paper Scizzors!")
    print("1) START")
    print("2) SIMULATION")
    
    try:
        while True:
            user_input = int(input())
            if user_input == 1:
                game_loop()
            elif user_input == 2:
                user_input_iterations = input("\nHow Many Iterations?: ")
                simulated_iterations(int(user_input_iterations))
            else:    
                print("Invalid Input")
    
        game_loop()

    except ValueError:
        print("ValueError: Invalid Input Type")

    print("Bye Bye!!!")

if __name__ == "__main__":
    print_title()
    
    
