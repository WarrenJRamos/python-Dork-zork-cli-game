
# pylint: disable=R0904
# The print methods that have "change this later" means that we are not
# using them for the current sprint. The disable above allows us to go over
# 20 public methods.

class Room1Printing():
    """ Print methods for all rooms """

    def print_move(room, direction):
        """
        Prints a statement to user after player moves a certain direction
        """
        if room == "room 1":
            if direction == "north":
                print("You enter the boss room.")
            if direction == "south":
                print("You cannot go/move south.")
            if direction == "east":
                print("There is a table in the room with a donut on top.")
            if direction == "west":
                print("There is a beautiful garden with the roadrunner's nest right \nin the center of the garden. The nest has eggs that look about \nready to hatch but no roadrunner parent to be seen.")

    def print_look(direction):
        """
        Prints a statement after user looks a certain direction
        """
        if direction == "north":
            print("There is a door with a sign that says DANGER.")
        if direction == "south":
            print("There is bag of bird food with all sorts of insects " +
                  "that roadrunners love to eat.")
        if direction == "east":
            print("To the East, there is a sign that says Lounge.")
        if direction == "west":
            print("To the West, there is a sign that says Roadrunner's Nest")

    @classmethod
    def print_score(cls, score):
        """
        Prints out the score
        """
        print("You have a score of " + str(score))

    @classmethod
    def print_diagnostic(cls, health_score):
        """
        Prints out the health data of the player
        """
        print("You have a health score of: " + str(health_score))

    def print_get(item):
        """
        Prints the item stored into player inventory
        """
        print("You put the " + item + " in your inventory")

    def print_read(item):
        """
        Prints the item that is being read.
        """
        if item == "paper":
            print("I don't like this bird. Dispose of it for me. - Dean")
        else:
            print(item + "was not found")

    @classmethod
    def print_drop_item(cls):
        """
        Print the item being dropped
        """
        print("CHANGE THIS FOR FUTURE SPRINT")

    @classmethod
    def print_open_item(cls, item):
        """
        Print what happens after player open the item.
        """
        print("You successfully open the " + item +
              ", and the bird hops on your shoulder. " +
              "The bird is added to your inventory.")
        # Call the add_inventory() method here

    @classmethod
    def print_move_moveable(cls):
        """
        Prints what happens after the item is moved
        """
        print("CHANGE THIS LATER")

    @classmethod
    def print_attack(cls, creature):
        """
        Prints out what happens after the player attacks a creature
        """
        if creature == "dean":
            print("You run up to the dean and start punching him. He is in " +
                  "lots of pain but was able to call security to take you away. GAME OVER.")
            from dork.commandManager import CommandManager
            CommandManager.setGameOver(True)
        else:
            print("You cannot attack " + creature)

    def print_examine(item):
        """
        Print out what happens when the player examines an item
        """
        if item == "paper":
            print("I don't "+ "like this bird. Dispose of it for me. - Dean")
        elif item == "roadrunner":
            print("The roadrunner is in bad condition. It looks starving and nervous.")
        elif item == "cage":
            print("The cage is tight, dirty, and locked.")
        else:
            print(item + " is unable to be examined")

    def print_inventory(inventory):
        """
        Print out the player's inventory
        """
        print("You currently have:")
        for items in inventory:
            print(items + " ")

    def print_eat_food(item):
        """
        Print out what happens after player eats item.
        """
        if item == "donut":
            print("The donut is yummy. Unfortunately, the player dies " +
                  "as THE DONUT IS POISONOUS!!! GAME OVER")
            from dork.commandManager import CommandManager
            CommandManager.setGameOver(True)
        else:
            print(item + "is not something you can eat.")

    def print_feed_creature(food):
        """
        Print what happens after player feeds the runner
        """
        if food == "donut":
            print("Through one of the tiny openings in the cage, you drop " +
                  "the donut into the cage. The roadrunner finished the donut " +
                  "AND DIES!!! You figure out the donut is poisonous! GAME OVER!")
            from dork.commandManager import CommandManager
            CommandManager.setGameOver(True)
        if food == "bird food":
            print("Through one of the tiny openings in the cage, you drop some " +
                  "bird food into the cage. The roadrunner eats the food and seems " +
                  "energized.")
        if food is None:
            print("There is nothing to feed the bird with.")

    @classmethod
    def print_give_item(cls):
        """
        Print what happens after player gives the item
        """
        print("CHANGE THIS LATER")