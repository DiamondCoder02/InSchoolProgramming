import json
print("\033c")

language=input("Language / Nyelv: Eng/Hun: \n")
#json config load
langfile = '.\\languages\\'+ language + '.json'
with open(langfile, 'r') as json_config:
    lang = json.load(json_config)
json_config.close
print(lang)
print(language)

again=input('Wanna play a game?' + '\n1.Yes \n2.No \n')
again=int(again)
while again == 1:
    print('Choose a gamemode:')
    gamemode=input('1. I think of a number \n2. You think of a number \n3. Exit \n')
    game = int(gamemode)
    if game > 0:
        if game == 1:
            import random
            mn=input('What is the biggest number you want to guess? \n')
            maxnumber= int(mn)
            num = random.randint(1, maxnumber)
            guess = None
            while guess != num:
                guess = input('Guess a number between 1 and ' + mn + ":")
                guess = int(guess)
                if guess < num:
                    print('Low guess')
                elif guess > num:
                    print('Guess is high')
                else:
                    print('You guessed it! Congratulations!')
                    break
        if game == 2:
            print("Whut:")
        if game == 3:
            break
        if game > 4:
            print('Please enter a valid number.')
        again=input('Want to play again?' + '\n1.Yes \n2.No \n')
        again=int(again)
    else:
        print("\033c")
        print('Please enter a valid number.')

print('\n ***Thank you for playing***')