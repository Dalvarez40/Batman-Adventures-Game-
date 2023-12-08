# Daniel Alvarez
# 12/6/23
# Chapter 5

import time
from GVars import batman
def start():
    # The array is the chapter 5 monologue for Batman adventures.
    text_array = ["\033[34m Once batman defeats all of Jokers goons he decides to have one last fight with the Joker. Batman wins. \033[0m",
                  "\033[34m However, the Clown Prince of crime had a backup plan.\033[0m",
                  "\033[34m Joker and Batman fight on top of the steel bridge.\033[0m"
                  "\033[34m Batman must choose who he saves between Robin and Batgirl.\033[0m"
                  "\033[34m Joker leaps off the window having a parachute and landing in a chopper to escape with his goons.\033[0m"]

    for text in text_array:
        print(text)
        time.sleep(0.5)

    while True:
        # This displays three options for the User to choose by entering 1, 2, or 3
        choice = input("Player actions: \n1 -Save Robin (Enter 1)\n2 - Save Batgirl (Enter 2)\n3 - Attempt to disarm bomb (Enter 3)")

        # Entering 1 will save robin and have a monologue for the ending.
        if choice == '1':
            print("Robin has been saved")
            text_array = ["\033[34m The aftermath of the fight left Batman feeling guilty for not saving Batgirl.\033[0m",
                          "\033[34m However, Batman gets a call from Batgirl revealing that she was indeed rescued by Nightwing.\033[0m",
                          "\033[34m Nightwing was tracking Batman from Blood haven City. .\033[0m",
                          "\033[34m Batman relieved and thrilled that Batgirl is alive is now on the hunt for the Joker with his Bat family.\033[0m",
                          "\033[34m END of Batman.\033[0m"]
            for text in text_array:
                print(text)
                time.sleep(2.5)

            # This will give users the option to restart the game
            batman.start_game()

        # Entering 2 will save Batgirl and have a monologue for the ending.
        elif choice == '2':
            print("Batgirl has been saved")
            text_array2 = ["\033[34m The aftermath of the fight and the steel mill blowing up leaves Batman guilty. \033[0m"
                          "\033[34m Batman feels ashamed for leaving someone who he considered as a son.\033[0m",
                          "\033[34m JNightwing arrives to the crime scene.\033[0m",
                          "\033[34m Nightwing claims that he was tracking batman but it was already to late.\033[0m",
                          "\033[34m Batman enraged, orders Nightwing to bring Batgirl back to the batcave.\033[0m",
                          "\033[34m Nightwing tells batman to calm down and worry about Batgirl first.\033[0m"
                          "\033[34m Batman ignores him and goes on the hunt to track down the Joker \033[0m"
                          "\033[34m Bad Ending: \033[0m"]

            for text in text_array2:
                print(text)
                time.sleep(2.5)
            batman.start_game()

        # If batman has exactly 45% or more health than he will save both heroes and have a monologue
        elif choice == '3':
            if batman.health <= 45:
                print("Batman successfully disarms bomb and batman frees Robin and Batgirl.")
                text_array = ["\033[34m Once batman defeats all of Jokers goons he decides to have one last fight with the Joker. \033[0m",
                              "\033[34m Batman wins, however, the Clown Prince of crime had a backup plan.\033[0m",
                              "\033[34m Joker and Batman fight on top of the steel bridge.\033[0m",
                              "\033[34m Batman must choose who he saves between Robin and Batgirl.\033[0m",
                              "\033[34m Joker leaps off the window having a parachute and landing in a chopper to escape with his goons.\033[0m"]
                for text in text_array:
                    print(text)
                    time.sleep(3.0)
                # This will give users the option to restart the game
                batman.start_game()

            # If Batman does not have exactly 45% health or more than he will have to choose the other two options
            else:
                print("Batman was unable to disarm the bomb.")
                print("Batman must choose between his two sidekicks")

                #
                while True:
                    # This displays two options for the User to choose by entering 1 or 2
                    choicesave = input("Player actions: \n1 -Save Robin (Enter 1)\n2 - Save Batgirl (Enter 2)")

                    # Entering 1 will save robin and have a monologue for the ending.
                    if choicesave == '1':
                        print("Batman has saved Robin")
                        text_array = ["\033[34m The aftermath of the fight left Batman feeling guilty for not saving Batgirl.\033[0m",
                                      "\033[34m However, Batman gets a call from Batgirl revealing that she was indeed rescued by Nightwing.\033[0m",
                                      "\033[34m Nightwing was tracking Batman from Blood haven City. .\033[0m",
                                      "\033[34m Batman relieved and thrilled that Batgirl is alive is now on the hunt for the Joker with his Bat family.\033[0m",
                                      "\033[34m END of Batman.\033[0m"]

                        for text in text_array:
                            print(text)
                            time.sleep(3.0)

                        # This will give users the option to restart the game
                        batman.start_game()

                    # Entering 2 will save Batgirl and have a monologue for the ending.
                    elif choicesave == '2':
                        print("Batman has saved Batgirl ")
                        text_array = ["\033[34m The aftermath of the fight and the steel mill blowing up leaves Batman guilty. \033[0m"
                                      "\033[34m Batman feels ashamed for leaving someone who he considered as a son.\033[0m",
                                      "\033[34m Nightwing arrives to the crime scene.\033[0m",
                                      "\033[34m Nightwing claims that he was tracking batman but it was already to late.\033[0m",
                                      "\033[34m Batman enraged, orders Nightwing to bring Batgirl back to the batcave.\033[0m",
                                      "\033[34m Nightwing tells batman to calm down and worry about Batgirl first.\033[0m"
                                      "\033[34m Batman ignores him and goes on the hunt to track down the Joker \033[0m"
                                      "\033[34m Bad Ending.\033[0m"]

                        for text in text_array:
                            print(text)
                            time.sleep(3.0)
                        # This will give users the option to restart the game
                        batman.start_game()

                    # If the user enters anything that is not from the choices then they will have to enter again
                    else:
                        print("Batman does not understand that course of action. Please enter a valid option.")


        # If the user enters anything but the choices provided, then they will have to enter again
        else:
            print("Batman does not understand that course of action. Please enter a valid option.")
#
#
