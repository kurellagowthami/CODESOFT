import random

def get_computer_choice():
    choices = ["rock","paper","scissor"]
    return random.choice(choices)
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "its a tie!"
    elif(
         (user_choice == "rock" and computer_choice == "scissor") or
         (user_choice == "paper" and computer_choice == "rock") or
         (user_choice == "scissor" and computer_choice == "paper")
    ):
        return "You Win"
    else:
        return "Computer Win"
def play_game():
    print("Welcome to Rock Paper Scissor!")
    while True:
        user_choice = input("Enter Your choice(rock,paper,scissor) or quit to exit: ").lower()
        if user_choice == "quit":
            print("thanks for playing!")
            break
        if user_choice not in ["rock","paper","scissor","quit"]:
            print("invalid choice.please try again")
            continue
        computer_choice = get_computer_choice()
        print(f"you choose :{user_choice}")
        print(f"computer choose :{computer_choice}")
        result = determine_winner(user_choice,computer_choice)
        print(result)
if __name__ == "__main__":
    play_game()
    
