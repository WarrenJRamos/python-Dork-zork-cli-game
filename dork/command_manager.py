"""This class acts as the controller for the game"""
from dork.room_printing import Room1Printing

INPUT_LINE = "" #Main Command
INPUT_HELPER = "" #Helper Command (usually an object)
GAME_OVER = False
   # HEALTH = 5
PLAYER_INVENTORY = [""]
class CommandManager:
    """cli controller"""
    INPUT_LINE = "" #Main Command
    INPUT_HELPER = "" #Helper Command (usually an object)
    GAME_OVER = False
   # HEALTH = 5
    PLAYER_INVENTORY = [""]

    def start(self):
        """
        Initialize Starting Variables
        """
        print("Welcome to Dork!")
        #global GAME_OVER
        #global INPUT_LINE
        #global HEALTH
        #global PLAYER_INVENTORY
        #GAME_OVER = False
        #PLAYER_INVENTORY = [""]

    def check_game_over(self):
        """
        Check if the game is over
        """
        #global GAME_OVER
        return GAME_OVER

    def set_game_over(self, cond):
        """
        Method for conditional termination of the game
        """
        #global GAME_OVER
        if cond is True:
            GAME_OVER = True
        if cond is not True:
            GAME_OVER = False

    def read_command(self):
        """
        Reads command from the console, translates and returns the command
        """
        global INPUT_LINE
        global INPUT_HELPER
        north = ['up', 'north', 'n'] #north
        south = ['down', 'south', 's'] #south
        east = ['east', 'e', 'right'] #est
        west = ['west', 'w', 'left'] #west
        move = ['move', 'walk', 'run', 'skip', 'hop', 'crawl', 'scoot', 'wander', 'go'] #go

        look = ['look', 'see', 'peer', 'view'] #examine
        get = ['grab', 'get', 'take'] #get
        put = ['put', 'set', 'lay'] #put

        eat = ['eat'] # Player eats
        feed = ['feed'] # -> Gives food
        inventory = ['inventory']



        #Shortcut checks & Dictionary breakdown
        INPUT_LINE = input("")
        if INPUT_LINE in north:
            INPUT_LINE = "go north"
        elif INPUT_LINE in south:
            INPUT_LINE = "go south"
        elif INPUT_LINE in east:
            INPUT_LINE = "go east"
        elif INPUT_LINE in west:
            INPUT_LINE = "go west"
        elif (INPUT_LINE[0:2] in move or INPUT_LINE[0:3] in move) and (len(INPUT_LINE) < 6):
            INPUT_LINE = "go"
        elif (INPUT_LINE[0:4] in move or INPUT_LINE[0:5] in move) and (len(INPUT_LINE) < 6):
            INPUT_LINE = "go"
        elif INPUT_LINE[0:3] in put:
            INPUT_HELPER = INPUT_LINE[4:len(INPUT_LINE)]
            INPUT_LINE = "put"
        elif INPUT_LINE[0:3] in get:
            INPUT_HELPER = INPUT_LINE[4:len(INPUT_LINE)]
            INPUT_LINE = "get"
        elif INPUT_LINE[0:4] in get:
            INPUT_HELPER = INPUT_LINE[5:len(INPUT_LINE)]
            INPUT_LINE = "get"
        elif INPUT_LINE[0:3] in look:
            INPUT_HELPER = INPUT_LINE[4:len(INPUT_LINE)]
            INPUT_LINE = "look"
        elif INPUT_LINE[0:4] in look:
            INPUT_HELPER = INPUT_LINE[5:len(INPUT_LINE)]
            INPUT_LINE = "look"
        elif INPUT_LINE[0:3] in eat:
            INPUT_HELPER = INPUT_LINE[4:len(INPUT_LINE)]
            INPUT_LINE = "eat"
        elif INPUT_LINE[0:4] in feed:
            INPUT_HELPER = INPUT_LINE[5:len(INPUT_LINE)]
            INPUT_LINE = "feed"
        elif INPUT_LINE in inventory:
            INPUT_LINE = "inventory"

    def execute_command(self):
        """
        Takes the command from previous method if valid and returns the result
        """
       # global GAME_OVER
        #global INPUT_LINE
        #global INPUT_HELPER
        #global PLAYER_INVENTORY
        room_one_prints = Room1Printing()
        #print(inputLine[0:2] + "   " + inputLine[3:8]) #Debugging
        if INPUT_LINE == "exit":
            print("Bye!")
            self.set_game_over(True)
        elif INPUT_LINE[0:8] == "go north":
            room_one_prints.print_move("room 1", "north")
        elif INPUT_LINE[0:8] == "go south":
            room_one_prints.print_move("room 1", "south")
        elif INPUT_LINE[0:7] == "go east":
            room_one_prints.print_move("room 1", "east")
        elif INPUT_LINE[0:7] == "go west":
            room_one_prints.print_move("room 1", "west")
        elif INPUT_LINE == "go":
            print("Go where?")
        elif INPUT_LINE == "look":
            room_one_prints.print_look("room 1", INPUT_HELPER)
            if INPUT_HELPER != "north" and INPUT_HELPER != "south" and INPUT_HELPER != "west" and INPUT_HELPER != "east":
                room_one_prints.print_examine(INPUT_HELPER)
        elif INPUT_LINE == "get":
            room_one_prints.print_get(INPUT_HELPER)
            PLAYER_INVENTORY.append(INPUT_HELPER)
        elif INPUT_LINE == "put":
            print("Put not ready")
        elif INPUT_LINE == "eat":
            room_one_prints.print_eat_food(INPUT_HELPER)
        elif INPUT_LINE == "feed":
            room_one_prints.print_feed_creature(INPUT_HELPER)
        elif INPUT_LINE == "inventory":
            room_one_prints.print_inventory(PLAYER_INVENTORY)
        else:
            print("Invalid Command!")
