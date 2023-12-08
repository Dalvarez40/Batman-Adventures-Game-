# Daniel Alvarez
# 12/6/23
# Chapter 2

import time
from GVars import batman

# Start of Chapter 2 for Batman Adventures
def start():
    # The array is the chapter 2 monologue for Batman adventures.
    text_array = ["\033[34m Batman enters the steel mill successfully enters the steel mill.\033[0m",
                  "\033[34m Alfred Contacts him and tell him that and Batgirl could be near by\033[0m",
                  "\033[34m However, he must decide what the best course of action is after he enters the steel mill\033[0m"]

    # This function allows the array to be displayed one sentence at a time at 2.5 seconds
    for text in text_array:
        print(text)
        time.sleep(2.5)

    # This displays three options for the User to choose by entering 1, 2, or 3
    while True:
        choice = input("Player actions: \n1 -Investigate the area (Enter 1)\n2 - Walk Forward (Enter 2)\n3 - Run Forward (Enter 3)")

        # Entering '1' will store the access code into the batman class and proceed to chapter 3
        if choice == '1':
            batman.tools.append("door code")
            print(batman.tools)
            print()
            break

        # Allows will move into chapter 3
        elif choice == '2':
            print("Batman has walked forward feeling guilty about what happened to Batgirl and Robin")
            break

        # Batman will fight and take 25% damage moving into chapter 3
        elif choice == '3':
            batman.damage(25)
            print("Batman has encountered some black mask goons")
            print("Batman has taken some damage.")
            break
        # Any other option that is not 1, 2, or 3 will display this message and will loop back to the options
        else:
            print("Batman does not understand that course of action. Please enter a valid option.")
    import chapter3
    chapter3.start()

if __name__ == "__main__":
    start()

