print("\033c")
print('Choose a gamemode:')
gamemode=input('1. I think of a number \n2. You think of a number: \n3. Exit \n')
game = int(gamemode)
while game < 4:
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
                print("nope, sorry. try again!")

    if game == 2:
        print("Whut:")
    if game == 3:
        break
    break
print('Thank you for playing')


"""
lang = None
plang = ["Hun", "Eng"]
while lang == plang:
    for lang in plang:
        print("Nyelv / Language:")
        lang=input('Eng, Hun \n')
        print(lang)
        continue
    continue
"""