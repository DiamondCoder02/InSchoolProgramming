print("\033c")
import json ; import os; import mouse; import keyboard
click=0; time=0; actualClick=0; clickMultiplier=1

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
        print("\033c" + "Write one of theses: eng, hun \nAlso don't forget tha language files. \n")
        
print(lang["welcome"])