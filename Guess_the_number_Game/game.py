print("\033c")
import json
import random
import os
to_play=1 ; wins1=0 ; wins2=0 ; lose1=0 ; lose2=0 ; what=0 ; win=False

while True:
    try:
        l=os.listdir('.\\languages')
        li=[x.split('.')[0] for x in l]
        language = str(input("Language / Nyelv: " + str(li) + "\n"))
        langfile = '.\\languages\\'+ language + '.json'
        with open(langfile, 'r', encoding='utf-8') as json_config:
            lang = json.load(json_config)
        json_config.close
        break
    except:
        print("\033c" + "Write one of theses: eng, hun, owo \nAlso don't forget tha language files. \n")
while to_play == 1:
    while True:
        try:
            again = int(input(lang["wanna_play"] + lang["YN"]))
            break
        except:
            print(lang["enter_valid"])
    if int(again) == 1:
        while int(again) == 1:
            while True:
                try:
                    print(lang["choose_gamemode"])
                    game=int(input(lang["menu"]))
                    break
                except:
                    print(lang["enter_valid"])
            print("\033c")
            if int(game) > 0 and int(game) < 4:
                if int(game) == 1:
                    mn=0
                    while int(mn) < 1:
                        while True:
                            try:
                                mn=int(input(lang["1_big_num"]))
                                break
                            except:
                                print(lang["enter_valid"])
                    num = random.randint(1, int(mn))
                    guess = 0
                    while int(guess) != num:
                        while True:
                            try:
                                trynum=int(input(lang["1_tries"]))
                                break
                            except:
                                print(lang["enter_valid"])
                        for x in range(int(trynum)):
                            while True:
                                try:
                                    guess=int(input(lang["guesses"] + str(x) + ') ' + lang["1_guess"] + str(mn) + ": "))
                                    print("\033c")
                                    break
                                except:
                                    print(lang["enter_valid"])
                            if int(guess) < num:
                                print(lang["low"])
                            elif int(guess) > num:
                                print(lang["high"])
                            else:
                                print(lang["1_won"])
                                wins1 += 1
                                break
                        else:
                            print(lang["1_failed_guess"] + str(num))
                            lose1 += 1
                            break
                elif int(game) == 2:
                    win = None ; mn=0
                    while mn < 1:
                        try:
                            mn=int(input(lang["2_big_num"]))
                            break
                        except:
                            print(lang["enter_valid"])
                    maxnumber = int(mn)
                    minnumber = 1
                    while True:
                        try:
                            trynum=int(input(lang["2_tries"]))
                            break
                        except:
                            print(lang["enter_valid"])
                    trynum1 = int(trynum)
                    guess = 0
                    while win != True:
                        for x in range(trynum1):
                            if minnumber > maxnumber:
                                print("The minimum cannot be bigger than max. Ending game.")
                                what += 1
                                win = True
                                break
                            while True:
                                try:
                                    num = random.randint(minnumber, maxnumber)
                                    #print(str(minnumber) +"NO"+ str(maxnumber))
                                    print(lang["guesses"] + str(x) + ') ' + lang["2_ask"] + str(num))
                                    guess=int(input("1. "+lang["low"]+"\n2. "+lang["high"]+"\n3. "+lang["correct"]+"\n"))
                                    print("\033c")
                                    break
                                except:
                                    print(lang["enter_valid"])
                            if int(guess) == 1:
                                minnumber = num+1
                                #print("lowering")
                            elif int(guess) == 2:
                                maxnumber = num-1
                                #print("Higher")
                            elif int(guess) == 3:
                                print(lang["2_comp_won"])
                                wins2 += 1
                                win = True
                                break
                            else:
                                print(lang["enter_valid"])
                        else:
                            print(lang["2_comp_fail"])
                            lose2 += 1
                            break
                elif int(game) == 3:
                    to_play = 0
                    break
                else:
                    print(lang["enter_valid"])
                while True:
                    try:
                        again=int(input(lang["want_again"] + lang["YN"]))
                        break
                    except:
                        print(lang["enter_valid"])
                to_play = 0
            else:
                print(lang["enter_valid"])
    elif int(again) == 2:
        to_play = 0
    else:
        print(lang["enter_valid"])

print(lang["thanks_playing"])
win1 = str(wins1) ; win2 = str(wins2) ; los1 = str(lose1) ; los2 = str(lose2)
print(lang["won1"] + win1 + "\n" + lang["lose1"] + los1 + "\n" + lang["won2"] + win2 + "\n" + lang["lose2"] + los2)
print("Whut? :" + str(what))