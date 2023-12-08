# Daniel Alvarez
# 12/6/23
# Chapter 1

# Start of Chapter 1 for Batman Adventures

import time
import random
#import GVars as gv
from GVars import batman
def start():
    # This is the drawing to the batman symbol that users see before playing the game.
    import turtle
    import math

    kalam = turtle.Turtle()
    kalam.speed(0)

    window = turtle.Screen()
    window.bgcolor("#000001")
    kalam.color("blue")

    ankur = 20

    kalam.left(90)
    kalam.penup()
    kalam.goto(-7 * ankur, 0)
    kalam.pendown()

    for a in range(-7 * ankur, -3 * ankur, 1):
        x = a / ankur
        rel = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                    math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
        kalam.goto(a, y * ankur)

    for a in range(-3 * ankur, -1 * ankur - 1, 1):
        x = a / ankur
        rel = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
            math.fabs(rel - 1) / (rel - 1))
        kalam.goto(a, y * ankur)

    kalam.goto(-1 * ankur, 3 * ankur)
    kalam.goto(int(-0.5 * ankur), int(2.2 * ankur))
    kalam.goto(int(0.5 * ankur), int(2.2 * ankur))
    kalam.goto(1 * ankur, 3 * ankur)
    print("Exit Screen when bat symbol is completed")
    for a in range(1 * ankur + 1, 3 * ankur + 1, 1):
        x = a / ankur
        rel = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
            math.fabs(rel - 1) / (rel - 1))
        kalam.goto(a, y * ankur)

    for a in range(3 * ankur + 1, 7 * ankur + 1, 1):
        x = a / ankur
        rel = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                    math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
        kalam.goto(a, y * ankur)

    for a in range(7 * ankur, 4 * ankur, -1):
        x = a / ankur
        rel = math.fabs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
        kalam.goto(a, y * ankur)

    for a in range(4 * ankur, -4 * ankur, -1):
        x = a / ankur
        rel = math.fabs(x)
        y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
        kalam.goto(a, y * ankur)

    for a in range(-4 * ankur - 1, -7 * ankur - 1, -1):
        x = a / ankur
        rel = math.fabs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
        kalam.goto(a, y * ankur)

    kalam.penup()
    kalam.goto(300, 300)

    turtle.done()

    # The array is the chapter 1 monologue for Batman adventures.
    text_array = ["\033[34mBatman returns after 3 years away from Gotham City.\033[0m",
                  "\033[34mBatman receives a phone call from Alfred claiming that Robin and Batgirl have gone missing.\033[0m",
                  "\033[34mThey have not been located and have not responded in 48 hours.\033[0m",
                  "\033[34mBatman arrives at the Wayne Manor and heads to the batcave.\033[0m",
                  "\033[34mWhen he gets down there he is greeted by a troubled Alfred.\033[0m",
                  "\033[34mHe immediately goes to check the Bat Computer.\033[0m",
                  "\033[34mBatman can't seem to locate Robin or Batgirl in Gotham.\033[0m",
                  "\033[34mBatman becomes frustrated and has only one option.\033[0m",
                  "\033[34mHe must go to a steel mill where Robin and Batgirl were last located.\033[0m",
                  "\033[34mBatman discovers that they were both together when they went missing.\033[0m",
                  "\033[34mHe discovers that they were on a mission to find a mysterious person.\033[0m",
                  "\033[34mA mysterious person going by the name Black Mask.\033[0m",
                  "\033[34mBatman finds out that Batgirl and Robin were last located in the steel mill.\033[0m",
                  "\033[34mBatman rushes over to the steel mill with the Batmobile.\033[0m",
                  "\033[34mHe arrives at the steel mill, but there are multiple of Black Mask's men.\033[0m",
                  "\033[34mHe must find a way inside the steel mill to investigate the area.\033[0m",
                  "\033[34mChoose your destiny.\033[0m"]

    # This function allows user to hit the enter before starting the game
    # This function gives the user time to get ready for the game
    enter = "click Enter to continue"
    print("Please to click enter when you are ready")
    input(enter)

    # This function allows the array to be displayed one sentence at a time at 2.5 seconds
    for text in text_array:
        print(text)
        time.sleep(2.5)
    steelmill()

# This function allows users to enter the steel mill
def steelmill():
    entermill = False
    while entermill == False:

        # This displays three options for the User to choose by entering 1, 2, or 3
        choice = input("Player actions: \n1 - Sneak Past the Guards(Enter 1)\n2 - Attack Guards(Enter 2)\n3 - Distarct Guards with Batmobile(Enter 3)\n")

        # This option allows the users to enter the steel mill with no damage
        if choice == "1":
            print("Batman found a secret entrance and has avoided unnecessary battle" )
            print("Batman has entered the steel mill.")
            entermill = True

        # This option has 50% chance for batman to get hurt while entering the steelmill
        elif choice == "2":
            if random.randint(1,10) > 5:
                print("The guards fight back, and Batman is hurt!")
                batman.damage(15)

            else:
                print("You beat the guards without breaking a sweat.")
                print("Batman has beaten all of black masks men.")
                print("Batman has entered the steel mill.")
            entermill = True

        # This option allows Batman to enter the steel mill but losing the batmobile in the story
        elif choice == "3":
            print("Batman uses the batmobile to distract the guards but loses it in the progress")
            print("Batman has entered the steel mill.")
            #gv.batman.batmobile = False
            batman.batmobile = False
            entermill = True

        # Any other option that is not 1, 2, or 3 will display this message and will loop back to the options
        else:
            print("Batman does not understand that course of action. enter a valid option")

    import chapter2
    chapter2.start()



