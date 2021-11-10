import json
import random
print("\033c")
#_______________________=to translate.

while True:
    try:
        language = str(input("Language / Nyelv: Eng/Hun: \n"))
        #json config load
        langfile = '.\\languages\\'+ language + '.json'
        with open(langfile, 'rb') as json_config:
            lang = json.load(json_config)
        json_config.close
        print(lang)
        print(langfile)
        print(language)
        break
    except:
        print("\033c")
        print("enter_valid")

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
            print("\033c")
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
                print("\033c")
                if game == 1:
                    maxnumber = 0
                    while maxnumber < 1:
                        while True:
                            try:
                                mn=int(input(lang["1_big_num"]))
                                break
                            except:
                                print("\033c")
                                print(lang["enter_valid"])
                        maxnumber= int(mn)
                    num = random.randint(1, maxnumber)
                    guess = None
                    print("\033c")
                    while guess != num:
                        while True:
                            try:
                                trynum=int(input(lang["1_tries"]))
                                break
                            except:
                                print("\033c")
                                print(lang["enter_valid"])
                        trynum1 = int(trynum)
                        for x in range(trynum1):
                            x1=str(x)
                            mn=str(mn)
                            while True:
                                try:
                                    guess=int(input(lang["guesses"] + x1 + ') ' + lang["1_guess"] + mn + ": "))
                                    break
                                except:
                                    print("\033c")
                                    print(lang["enter_valid"])
                            guess = int(guess)
                            if guess < num:
                                print(lang["low"])
                            elif guess > num:
                                print(lang["high"])
                            else:
                                print("\033c")
                                print(lang["1_won"])
                                wins1 += 1
                                break
                        else:
                            num1 = str(num)
                            print(lang["1_failed_guess"] + num1)
                            lose1 += 1
                            break
                elif game == 2:
                    print("Whut:(Not done yet)")
                    while True:
                        try:
                            mn=int(input(lang["2_big_num"]))
                            break
                        except:
                            print("\033c")
                            print(lang["enter_valid"])
                    maxnumber = int(mn)
                    minnumber = 1
                    while True:
                        try:
                            trynum=int(input(lang["2_tries"]))
                            break
                        except:
                            print("\033c")
                            print(lang["enter_valid"])
                    trynum1 = int(trynum)
                    guess = None
                    win = False
                    print("\033c")
                    while win != True:
                        for x in range(trynum1):
                            while True:
                                try:
                                    num = random.randint(minnumber, maxnumber)
                                    x1=str(x)
                                    num1=str(num)
                                    minnumber1=str(minnumber)
                                    maxnumber1=str(maxnumber)
                                    print(minnumber1 +"NO"+ maxnumber1)
                                    print(lang["guesses"] + x1 + ') ' + lang["2_ask"] + num1)
                                    guess=int(input("1. "+lang["low"]+"\n2. "+lang["high"]+"\n3. "+lang["correct"]+"\n"))
                                    break
                                except:
                                    print("\033c")
                                    print(lang["enter_valid"])
                            if guess == 1:
                                minnumber = num
                                print("lowering")
                            elif guess == 2:
                                maxnumber = num
                                print("High")
                            elif guess == 3:
                                print("Win")
                                wins2 += 1
                                win = True
                                break
                            else:
                                print("\033c")
                                print(lang["enter_valid"])
                        else:
                            num1 = str(num)
                            print(lang["2_comp_fail"] + num1)
                            lose2 += 1
                            break
                elif game == 3:
                    to_play = 0
                    break
                else:
                    print(lang["enter_valid"])
                while True:
                    try:
                        again=int(input(lang["want_again"] + lang["YN"]))
                        break
                    except:
                        print("\033c")
                        print(lang["enter_valid"])
                again=int(again)
                to_play = 0
            else:
                print("\033c")
                print(lang["enter_valid"])
    elif again == 2:
        to_play = 0
    else:
        print("\033c")
        print(lang["enter_valid"])

print(lang["thanks_playing"])
win1 = str(wins1)
win2 = str(wins2)
los1 = str(lose1)
los2 = str(lose2)
print(lang["won1"] + win1 + "\n" + lang["lose1"] + los1)
print(lang["won2"] + win2 + "\n" + lang["lose2"] + los2)