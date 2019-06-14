# Room Printing
# pylint: disable=R0904

class Room1Printing():
    """ Print methods for Room 1 - Entrance (Student Success Building) """

    @classmethod
    def print_move(cls, direction):
        """ 
        Prints a statement to user after player moves a certain direction
        """
        if direction == "north":
            print("You enter the boss room.")
        if direction == "south":
            print("You cannot go/move south.")
        if direction == "east":
            print("There is a table in the room with a donut on top.")
        if direction == "west":
            print("There is a beautiful garden with the roadrunner’s nest right " +
                  "in the center of the garden. The nest has eggs that look about " +
                  "ready to hatch but no roadrunner parent to be seen.")

    @classmethod
    def print_look(cls, direction):
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
            print("To the West, there is a sign that says Roadrunner’s Nest")

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

    @classmethod
    def print_get(cls, item):
        """
        Prints the item stored into player inventory
        """
        print("You put the " + item + " in your inventory")

    @classmethod
    def print_read(cls, item):
        """
        Prints our the item that is being read.
        """
        print()

    @classmethod
    def print_drop_item(cls):
        """
        """
        pass

    @classmethod
    def print_open_openeable(cls):
        """
        """
        pass

    @classmethod
    def print_move_moveable(cls):
        """
        """
        pass

    @classmethod
    def print_attack(cls):
        """
        """ 
        pass

    @classmethod
    def print_examine(cls):
        """
        """
        pass

    @classmethod
    def print_inventory(cls):
        """
        """
        pass

    @classmethod
    def print_eat_food(cls):
        """
        """
        pass

    @classmethod
    def print_feed_create(cls):
        """
        """
        pass

    @classmethod
    def print_release_creature(cls):
        """
        """        
        pass

    @classmethod
    def print_give_item(cls):
        """
        """
        pass