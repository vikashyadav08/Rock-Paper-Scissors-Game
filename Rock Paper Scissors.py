"""Rock Paper Scissors Game"""
'''1 for Rock -1 for Paper 0 for scissors'''
import random

count = 1
while count < 10:
    try:
        computer = random.choice([-1, 0, 1])
        youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
        
        youDict = {"r": 1, "p": -1, "s": 0}
        reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

        if youstr not in youDict:
            raise ValueError("Invalid input")

        you = youDict[youstr]

        print(f"You chose {reverseDict[you]}")
        print(f"Computer chose {reverseDict[computer]}")

        result = you - computer

        if result == 0:
            print("It's a draw!")
        elif result == 1 or result == -2:
            print("You win!")
        else:
            print("You lose!")

        count += 1

    except Exception as e:
        print("You entered wrong input. Try again.")
