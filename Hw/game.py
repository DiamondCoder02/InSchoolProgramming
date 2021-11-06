import json
print("\033c")
#_______________________=to translate.

#try:
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
                trynum=input('_______________________\nHow many tries you need to quess? \n')
                trynum1 = int(trynum)
                for x in range(trynum1):
                    guess = input('Guess a number between 1 and ' + mn + ":" + '  ('+x+')')
                    guess = int(guess)
                    if guess < num:
                        print('Low guess')
                    elif guess > num:
                        print('Guess is high')
                    else:
                        print("\033c")
                        print('You guessed it! Congratulations!')
                        break
                else:
                    num1 = str(num)
                    print('_____________________\nYou could not guess it. I\'m sorry. The number was: ' + num1)
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
#except:
 #   print('_____________________\nSomething went wrong. Restart the game and give correct numbers!')

print('\n___***Thank you for playing***___')