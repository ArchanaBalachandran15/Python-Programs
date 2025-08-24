import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to the Dice Roller!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"\nYou rolled a {result} 🎉")

        choice = input("Roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
