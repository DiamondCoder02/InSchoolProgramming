from itertools import product
import keyboard

keyboard.press_and_release('shift+s, space')

keyboard.write('The quick brown fox jumps over the lazy dog.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')


while True:
    print("\033c")
    test=0
    print("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    {}
    """.format(test))
    ans=input("What would you like to do? ")
        
    if ans=="1":
      print("\nStudent Added")
      break
    elif ans=="2":
      print("\n Student Deleted")
      break
    elif ans=="3":
      print("\n Student Record Found")
      break
    elif ans=="4":
      print("\n Goodbye") 
      break
    else:
       print("\n Not Valid Choice Try again")