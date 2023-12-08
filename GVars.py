# Daniel Alvarez
# 12/6/23

# Holds global variables and character class

#Creator of Batman Class
class Batman:
    def __init__(self):
        self.health = 100  # Batman's Health
        self.tools = []  # Holds the code that batman has in chapter 3

    def damage(self,damage): # Batman's decrease in health function
        self.health -= damage # The damage output to batman's health
        print("Health remaining:", self.health) # Displays Batman's health when he takes damage
        # If batman's health reaches ero then it would be game over
        if self.health <= 0:
            self.gameover()

    def hp (self,hp): # Batman's health recovery of health function
        self.health += hp # Batman's health increases
        print("Health remaining:", self.health) #

    def gameover(self): # Game Over Function
        choice = input("\033[91mYou have died. Do you want restart (Y) or end the game?\033[91m") # Diplays game over function

        # This allows users to restart the game  from Chapter 1 by entering "Y" or end game by clicking anything else
        if choice.upper() == "Y":
            import chapter1
            chapter1.start()
        else:
            exit()

    def start_game(self): # This a restart game function for Chapter 5

        # This allows users to restart the game based on their chapter 5 decisions
        choice = input(" Do you want to restart the adventure (Y) or end game?")
        if choice.upper() == "Y":
            import chapter1
            chapter1.start()
        else:
            exit()

global batman
batman = Batman()
