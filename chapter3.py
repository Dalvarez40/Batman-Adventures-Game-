# Daniel Alvarez
# 12/6/23
# Chapter 3


import time, chapter4
from GVars import batman
# Start of Chapter 12 for Batman Adventures
def start():
    # The array is the chapter 3 monologue for Batman adventures.
    text_array = ["\033[34m Batman is told by Alfred that Robin and Batgirl have started a family together.\033[0m",
                  "\033[34m Alfred contacts him and tells him that Robin and Batgirl could potentially be up ahead.\033[0m",
                  "\033[34m Batman keeps this in mind. As he gets told this he encounters a guarded door that has a password to it\033[0m"]

    # This function allows the array to be displayed one sentence at a time at 2.5 seconds
    for text in text_array:
        print(text)
        time.sleep(2.5)
    # If the door code is in batman class then the below message will display
    if "door code" in batman.tools:
        print("You have the door code!")

    # This displays three options for the User to choose by entering 1, 2, or 3
    while True:
        choice = input("Player actions: \n1 - Destroy Security Door  (Enter 1)\n2 - Call Alfred for Help (Enter 2)\n3 - Attempt Code (Enter 3)")

        # Batman will lose all of his health and players will have the option to restart the game.
        if choice == '1':
            print("Batman smashes the door down but has detonated 100 bombs in the process.")
            print("Game Over")
            batman.damage(100)


        elif choice == '2':
            print("Batman has contacted Alfred and asks him there is a way in: ")

            # If the door code is in the batman class then user will be told again and be granted 30 health
            if "door code" in batman.tools:
                print("Alfred has told batman the code is 1940: ")
                print("Batman thanks Alfred. Alfred sends batman a health kit. ")
                batman.hp(30)

                # The user will have to enter code based on the message they read
                print("Enter code the 4 digit code Alfred said")
                code2 = input("Enter code")

                # If the code 1940 is entered then player will move on to chapter  4
                if code2== '1940':
                    print("Batman has successfully entered the code ")
                    chapter4.start()
                # If the wrong code entered then this message will play
                else:
                    print("You have entered the wrong code: Try entering the code Alfred gave Batman")

            # If the code is not in batman class then it will display this message below
            else:
                print("Alfred tells Batman that Black mask has given the door a specific code from a criminal that they faced in their first year encounter")
                print("Alfred suggests Batman to either return to the steel mill or attempt the code")

                # This option will allow the user to return to chapter 2 or enter a 4-digit code
                choice3 = input("Player actions: \n1 -Return to previous area (Enter 2) \n2 - Attempt Code (Enter 1)")
                if choice3 == '1':
                    import chapter2
                    chapter2.start()
                if choice3 == '2':
                    entercode()

        elif choice == '3':
            print("Batman attempts to hack the security door")

            # if code is in batman class then the user will move onto chapter 4
            if "door code" in batman.tools:
                print("You have successfully opened the door the code  ")
                chapter4.start()

            # If the door code is not in batman class then the user is presented three options to select from
            else:
                print("Batman does not know the code and has entered incorrect code")
                while True:
                    choice2 = input("Player actions: \n1 - Return back and investigate the area (Enter 1)\n2 - Attempt code (Enter 2)  ")

                    # Entering choice 1 will send user back to chapter 2
                    if choice2 == '1':
                        print("Batman has gone back to the front entrance of the steel mill to investigate the area ")
                        import chapter2
                        chapter2.start()

                    # Entering choice will give the user a chance to enter a 4-digit code
                    elif choice2 == '2':
                        entercode()
                    else:
                        print("Batman does not understand that course of action. Please enter a valid option.")



def entercode():
    # If players attempt the code then this riddle will be displayed to help the user figure out the code
    text_array2 = ["Enter a 4 digit code: here's a riddle",
                   "Within the ink of Gotham's night,",
                   "A debut tale, a character's flight",
                   "In pages turned, a secret's told,",
                   "What year's embrace does it hold?",

                   "A trickster's grin, a mystery veiled",
                   "In purple shadows, a story unveiled",
                   "Detect the digits, sly and sly.",
                   "The answer hides, but can't deny."]
    for i in text_array2:
        print(i)
    # This function will give the player 3 chances to enter the code and will resolve based on their response
    counter = 2
    while counter > 0:
        code = input("Enter Code")

        # if code is correct then it will move to chapter 4
        if code == '1940': # This a 4-digit code that will give access proceed to chapter 4
            print("You have entered the correct code")
            failedcode = False
            counter = 0
            chapter4.start()
        # If the code is incorrect 3 times in a row then player will take 25% damage moving back to Chapter 2
        else:
            print("You have entered the wrong code", counter, "chances left")
            counter -= 1
            failedcode = True
    if failedcode:
        print("You have run out of chances to enter the code")
        print("Batman has taken 25 percent damage from the security system of door.")
        print("Batman forced to go back to the front entrance of the steel mill")
        batman.damage(25)
        import chapter2
        chapter2.start()






    #import chapter2
    #chapter2.start()


#start()
# text_array = []
# enter = "click Enter to continue"
#
# for text in text_array:
#     print(text)
#     input(enter)