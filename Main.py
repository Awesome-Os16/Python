import random

def display_welcome():
    print("\nHello! Welcome to KhadKhade")
    print("- Awesome Dahal (Developer/Owner)")
    print("\n1. Play the game")
    print("2. Exit")

def get_user_choice():
    while True:
        choice = input("\nChoose an option (1 or 2): ").strip()
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter 1 to play or 2 to exit.")
#Dont forget to save it idiot
def display_rules():
    print("\nIn this simplified version, you'll bet on the outcome of a random event.")
    print("You can place a bet on either 'heads' or 'tails'.")
    print("The game will randomly choose between 'heads' or 'tails' and if your bet matches the outcome, you win!\n")

def get_user_bet():
    while True:
        bet = input("Place your bet (heads/tails): ").strip().lower()
        if bet in ['heads', 'tails']:
            return bet
        else:
            print("Invalid bet. Please choose 'heads' or 'tails'.")

#bugfixes at "Fixies Code" notepad
def play_game():
    outcomes = ['heads', 'tails']
    result = random.choice(outcomes)
    
    user_bet = get_user_bet()
    
    print("\nThe result is:", result)
    
    if user_bet == result:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time!")

def main():
    while True:
        display_welcome()
        choice = get_user_choice()
        
        if choice == '1':
            display_rules()
            play_game()
            while input("\nDo you want to play again? (y/n): ").strip().lower() == 'y':
                play_game()
        elif choice == '2':
            print("Thank you for playing KhadKhade!")
            break

if __name__ == "__main__":
    main()



#Awesome is the GOAT


#thank you