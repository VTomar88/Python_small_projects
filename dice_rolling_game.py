from random import randint
while True:
    user_input = input("Roll the dice? (y/n): ")
    if user_input == 'n':
        print('Thanks for playing!')
        break
    elif user_input == 'y':
        print(f"({randint(1,6)}, {randint(1,6)})")
    else:
        print("Invalid choice!")

