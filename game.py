import random
#importing the random module to allow the computer to make random choices
user_score = 0
computer_score = 0
#initializing the scores for both the user and the computer to zero
choices = ["rock", "paper", "scissors"]
#defining the possible choices for the game in a list
while True:
#starting an infinite loop to allow the game to continue until the user decides to quit
    computer_choice = random.choice(choices)
    #the computer randomly selects a choice from the list of options
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    #prompting the user to enter their choice and converting it to lowercase for consistency
    if user_choice == 'quit':
        #if the user types 'quit', the game will end and a goodbye message will be displayed
        print("Thanks for playing!")
        break
        #the break statement exits the loop, ending the game
    elif user_choice not in choices:
        #if the user's input is not one of the valid choices, an error message will be displayed and the loop will continue to prompt for a valid choice
        print("Invalid choice. Please try again.")
        continue
        #the continue statement skips the rest of the loop and starts the next iteration, prompting the user again for a valid choice
    elif user_choice == computer_choice:
        print(f"Both chose {user_choice}. It's a tie!")
        #the f in the print statement allows for string interpolation, inserting the value of user_choice into the message to indicate that both the user and computer made the same choice, resulting in a tie
    else:
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:           
            print("Computer wins!")
            computer_score += 1  
    print(f"Score: You {user_score} - Computer {computer_score}")   
    computer_choice = random.choice(choices)
