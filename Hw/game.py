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
print(langfile)
print(language)

wins1=0
wins2=0
again=input(lang["wanna_play"] + lang["YN"])
again=int(again)
while again == 1:
    print(lang["choose_gamemode"])
    gamemode=input(lang["menu"])
    game = int(gamemode)
    if game > 0:
        if game == 1:
            import random
            mn=input(lang["1_big_num"])
            maxnumber= int(mn)
            num = random.randint(1, maxnumber)
            guess = None
            while guess != num:
                trynum=input('_______________________\nHow many tries you need to quess? \n')
                trynum1 = int(trynum)
                for x in range(trynum1):
                    x1=str(x)
                    guess = input('____________(Guesses:'+x1+') '+ lang["1_guess"] + mn + ": ")
                    guess = int(guess)
                    if guess < num:
                        print(lang["low"])
                    elif guess > num:
                        print(lang["high"])
                    else:
                        print("\033c")
                        print(lang["won"])
                        wins1 += 1
                        break
                else:
                    num1 = str(num)
                    print('_____________________\nYou could not guess it. I\'m sorry. The number was: ' + num1)
                    break
        elif game == 2:
            print("\033c")
            print("Whut:")
            wins2 += 1
        elif game == 3:
            break
        else:
            print(lang["enter_valid"])
        again=input(lang["want_again"] + lang["YN"])
        again=int(again)
    else:
        print("\033c")
        print(lang["enter_valid"])

#except:
 #   print('_____________________\nSomething went wrong. Restart the game and give correct numbers!')

print(lang["thanks_playing"])
win1 = str(wins1)
win2 = str(wins2)
print('________________You won: ' + win1 + '\n________________I, the computer won: ' + win2)