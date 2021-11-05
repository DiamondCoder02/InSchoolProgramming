print("\033c")
again = "y"
while again == "y":
    print('Choose a gamemode:')
    gamemode=input('1. I think of a number \n2. You think of a number \n3. Exit \n')
    game = int(gamemode)
    if game < 4:
        if game == 1:
            import random
            num = random.randint(1, 10)
            guess = None
            while guess != num:
                guess = input("guess a number between 1 and 10: ")
                guess = int(guess)

                if guess == num:
                    print("You won!")
                    break
                else:
                    print("Nope, sorry. Try again!")
        if game == 2:
            print("Whut:")
        if game == 3:
            break
        again=input('Want to play again? (y/n): ')
    else:
        print("\033c")
        print("Give me a valid option:")
print('Thank you for playing')