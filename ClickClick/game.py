print("\033c")
import json ; import os; import mouse; import keyboard
click=0; time=0; actualClick=0; clickMultiplier=1; game=True

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

#Time to learn python classes
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
print(p1.name)
print(p1.age)

print("-----------------------------------------------------------")
#I think I know classes! Don't judge naming. It is just to better understand it.
class test:
  def __init__(gay, hi, fuck):
    gay.hello = hi
    gay.sex = fuck
    
  def lol(gay):
    print("Hi, I'm " + str(gay.sex) + " and I want to intercourse " + gay.hello)

text = test("You", 18)
print(text.hello)
print(text.sex)
text.lol()