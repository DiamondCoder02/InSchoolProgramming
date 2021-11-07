import json
import random
print("\033c")
#_______________________=to translate.

language=input("Language / Nyelv: Eng/Hun: \n")
#json config load
langfile = '.\\languages\\'+ language + '.json'
with open(langfile, 'rb') as json_config:
    lang = json.load(json_config)
json_config.close
print(lang)
print(langfile)
print(language)

to_play = 1
while to_play == 1:
    wins1=0
    wins2=0
    lose1=0
    lose2=0
    while True:
        try:
            again = int(input(lang["wanna_play"] + lang["YN"]))
            break
        except:
            print(lang["enter_valid"])
    again=int(again)
    if again == 1:
        print("\033c")
        while again == 1:
            while True:
                try:
                    print(lang["choose_gamemode"])
                    gamemode=int(input(lang["menu"]))
                    break
                except:
                    print("\033c")
                    print(lang["enter_valid"])
            game = int(gamemode)
            if game > 0 and game < 4:
                if game == 1:
                    maxnumber = 0
                    while maxnumber < 1:
                        mn=input(lang["1_big_num"])
                        maxnumber= int(mn)
                    num = random.randint(1, maxnumber)
                    guess = None
                    print("\033c")
                    while guess != num:
                        trynum=input(lang["1_tries"])
                        trynum1 = int(trynum)
                        for x in range(trynum1):
                            x1=str(x)
                            guess = input(lang["1_guesses"] + x1 + ') ' + lang["1_guess"] + mn + ": ")
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
                            print(lang["1_failed_guess"] + num1)
                            lose1 += 1
                            break
                elif game == 2:
                    print("\033c")
                    print("Whut:")
                    wins2 += 1
                    lose2 += 2
                elif game == 3:
                    to_play = 0
                    break
                else:
                    print(lang["enter_valid"])
                again=input(lang["want_again"] + lang["YN"])
                again=int(again)
                to_play = 0
            else:
                print("\033c")
                print(lang["enter_valid"])
    elif again == 2:
        to_play = 0
    else:
        print(lang["enter_valid"])

print(lang["thanks_playing"])
win1 = str(wins1)
win2 = str(wins2)
los1 = str(lose1)
los2 = str(lose2)
print(lang["won1"] + win1 + "\n" + lang["lose1"] + los1)
print(lang["won2"] + win2 + "\n" + lang["lose2"] + los2)