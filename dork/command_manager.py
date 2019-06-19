"""This class acts as the controller for the game"""
from dork.room_printing import Room1Printing
#INPUT_LINE = ""
#INPUT_HELPER = ""
#GAME_OVER = False
#PLAYER_INVENTORY = [""]
class CommandManager:
    """cli controller"""

    def __init__(self):
        self.GAME_OVER = False
        self.INPUT_LINE = ""
        self.INPUT_HELPER = ""
        self.PLAYER_INVENTORY = [""]

    def start(self):
        """
        Initialize Starting Variables
        """
        print("Welcome to Dork!")

    def check_game_over(self):
        """
        Check if the game is over
        """
        return self.GAME_OVER

    def set_game_over(self, cond):
        """
        Method for conditional termination of the game
        """
        if cond is True:
            self.GAME_OVER = True
        if cond is not True:
            self.GAME_OVER = False

    def read_command(self):
        """
        Reads command from the console, translates and returns the command
        """

        north = ['up', 'north', 'n']
        south = ['down', 'south', 's']
        east = ['east', 'e', 'right']
        west = ['west', 'w', 'left']
        move = ['move', 'walk', 'run', 'skip', 'hop', 'crawl', 'scoot', 'wander', 'go']

        look = ['look', 'see', 'peer', 'view']
        get = ['grab', 'get', 'take']
        put = ['put', 'set', 'lay']

        eat = ['eat']
        feed = ['feed']
        inventory = ['inventory']

        self.INPUT_LINE = input("")
        if self.INPUT_LINE in north:
            self.INPUT_LINE = "go north"
        elif self.INPUT_LINE in south:
            self.INPUT_LINE = "go south"
        elif self.INPUT_LINE in east:
            self.INPUT_LINE = "go east"
        elif self.INPUT_LINE in west:
            self.INPUT_LINE = "go west"
        elif (self.INPUT_LINE[0:2] in move or self.INPUT_LINE[0:3] in move) and (len(self.INPUT_LINE) < 6):
            self.INPUT_LINE = "go"
        elif (self.INPUT_LINE[0:4] in move or self.INPUT_LINE[0:5] in move) and (len(self.INPUT_LINE) < 6):
            self.INPUT_LINE = "go"
        elif self.INPUT_LINE[0:3] in put:
            self.INPUT_HELPER = self.INPUT_LINE[4:len(self.INPUT_LINE)]
            self.INPUT_LINE = "put"
        elif self.INPUT_LINE[0:3] in get:
            self.INPUT_HELPER = self.INPUT_LINE[4:len(self.INPUT_LINE)]
            self.INPUT_LINE = "get"
        elif self.INPUT_LINE[0:4] in get:
            self.INPUT_HELPER = self.INPUT_LINE[5:len(self.INPUT_LINE)]
            self.INPUT_LINE = "get"
        elif self.INPUT_LINE[0:3] in look:
            self.INPUT_HELPER = self.INPUT_LINE[4:len(self.INPUT_LINE)]
            self.INPUT_LINE = "look"
        elif self.INPUT_LINE[0:4] in look:
            self.INPUT_HELPER = self.INPUT_LINE[5:len(self.INPUT_LINE)]
            self.INPUT_LINE = "look"
        elif self.INPUT_LINE[0:3] in eat:
            self.INPUT_HELPER = self.INPUT_LINE[4:len(self.INPUT_LINE)]
            self.INPUT_LINE = "eat"
        elif self.INPUT_LINE[0:4] in feed:
            self.INPUT_HELPER = self.INPUT_LINE[5:len(self.INPUT_LINE)]
            self.INPUT_LINE = "feed"
        elif self.INPUT_LINE in inventory:
            self.INPUT_LINE = "inventory"

    def execute_command(self):
        """
        Takes the command from previous method if valid and returns the result
        """
        room_one_prints = Room1Printing()
        #print(inputLine[0:2] + "   " + inputLine[3:8]) #Debugging
        if self.INPUT_LINE == "exit":
            print("Bye!")
            self.set_game_over(True)
        elif self.INPUT_LINE[0:8] == "go north":
            room_one_prints.print_move("room 1", "north")
        elif self.INPUT_LINE[0:8] == "go south":
            room_one_prints.print_move("room 1", "south")
        elif self.INPUT_LINE[0:7] == "go east":
            room_one_prints.print_move("room 1", "east")
        elif self.INPUT_LINE[0:7] == "go west":
            room_one_prints.print_move("room 1", "west")
        elif self.INPUT_LINE == "go":
            print("Go where?")
        elif self.INPUT_LINE == "look":
            room_one_prints.print_look("room 1", self.INPUT_HELPER)
            direction = ['north', 'south', 'east', 'west']
            if self.INPUT_HELPER not in direction:
                room_one_prints.print_examine(self.INPUT_HELPER)
        elif self.INPUT_LINE == "get":
            room_one_prints.print_get(self.INPUT_HELPER)
            self.PLAYER_INVENTORY.append(self.INPUT_HELPER)
        elif self.INPUT_LINE == "put":
            print("Put not ready")
        elif self.INPUT_LINE == "eat":
            room_one_prints.print_eat_food(self.INPUT_HELPER)
        elif self.INPUT_LINE == "feed":
            room_one_prints.print_feed_creature(self.INPUT_HELPER)
        elif self.INPUT_LINE == "inventory":
            room_one_prints.print_inventory(self.PLAYER_INVENTORY)
            print("Inventory:")
        else:
            print("Invalid Command!")
