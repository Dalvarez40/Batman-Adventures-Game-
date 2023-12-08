# Daniel Alvarez
# 12/6/23
# Chapter 4

import time, chapter5
from GVars import batman

# Start of Chapter 12 for Batman Adventures
def start():
    # The array is the chapter 4 monologue for Batman adventures.
    text_array = ["\033[34m After Batman gets past the guarded door, he finds a broken elevator.\033[0m",
                  "\033[34m Batman glides down the elevator.\033[0m",
                  "\033[34m Waiting for him below is Black mask.\033[0m",
                  "\033[34m Batman confronts Black mask.\033[0m",
                  "\033[34m Black mask welcomes back batman or as he claims Bruce Wayne.\033[0m",
                  "\033[34m Black mask starts to laughs manically .\033[0m",
                  "\033[34m Black mask turns around to take off his disguise and reveals himslef to be the Joker.\033[0m",
                  "\033[34m The Joker confirms that he knows about the Wayne family.\033[0m",
                  "\033[34m Since Batman was gone from Gotham, the joker had a lot of time to make a plan.\033[0m",
                  "\033[34m The Joker thought about how he could make Batman return.\033[0m",
                  "\033[34m The Joker while in arkham was told the indinety of batman by former enemy of batman.\033[0m",
                  "\033[34m Dr. Hugo Strange.\033[0m",
                  "\033[34m The Joker was told all of Bruce Wayne's secrets.\033[0m",
                  "\033[34m The Joker thought about his plan and to escape arkham.\033[0m",
                  "\033[34m The Jokers plan was to kidnap the bat family starting with Robin and Batgirl.\033[0m",
                  "\033[34m The Joker knew this would force Batman to return. \033[0m",
                  "\033[34m The Joker wanted batman to return so that he could play into his twisted games.\033[0m",
                  "\033[34m The Joker wants Batman to suffer for leaving him without a hero to stop him..\033[0m",
                  "\033[34m The Joker wants punish batman by killing his family.\033[0m",
                  "\033[34m The Joker reveals two electric cells that contain Robin and Batgirl.\033[0m",
                  "\033[34m Batman must get to the cells to save Robin and Batgirl.\033[0m",
                  "\033[34m However the Joker is not alone\033[0m",
                  "\033[34m Along with him is also The Mad Hatter, Harley Quinn, and Clayface.\033[0m",
                  "\033[34m Batman must determine who he wants to takedown first.\033[0m"]

    for text in text_array:
        print(text)
        time.sleep(2.5)
    # This a list listin three batman villains
    bosslist = ["1: Harley Quinn", "2: Mad Hatter", "3: Clayface"]
    import random
    while bosslist != []:
        for i in bosslist:
            print(i)

        # Entering the 1 will enter a battle and will have a 50% chance of taking damage removing from the list
        choice = input("Please Enter 1 2 or 3")
        if choice == '1':
            bosslist.remove("1: Harley Quinn")
            print("Batman has defeated Harley Quinn")

            if random.randint(1, 10) > 5:
                print("Batman has taken damage from the fight")
                batman.damage(45)
            else:
                print("Batman has beaten the villain and has walked away unscathed.")

            print("Batman has defeated Harley Quinn.")

        # Entering the 3 will enter a battle and will give 35% health back to batman
        elif choice == '2':
            bosslist.remove("2: Mad Hatter")
            print("Batman has knocks down the Mad Hatter with easy and has taken his health potion.")
            batman.hp(35)
            print("Batman has defeated  Mad Hatter.")

        # Entering the 3 will enter a battle and will have a 35% chance of taking damage removing from the list
        elif choice == '3':
            bosslist.remove("3: Clayface")

            if random.randint(1, 10) > 5:
                print("Batman has taken damage from the fight")
                batman.damage(40)
            else:
                print("Batman has beaten the villain and has walked away unscathed.")

            print("Batman has defeated Clayface.")
        # Anything that is not 1,2, or 3 will be denied
        else:
            print("Invalid choice. Please select a valid option.")

    # After the list is done it will move to chapter 5
    chapter5.start()



















