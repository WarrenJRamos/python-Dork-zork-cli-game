#Command keyword arrays
from dork.room_printing import Room1Printing
class CommandManager:

    inputLine = "" #Main Command
    inputHelper = "" #Helper Command (usually an object)
    gameOver = False
    health = 5
    playerInventory = [""]

    def start(self):
        print("Welcome to Dork!")
        global gameOver
        global inputLine
        global health
        global playerInventory
        gameOver = False
        playerInventory = [""]

    def checkGameOver(self):
        global gameOver
        if gameOver == True:
            return True
        else:
            return False

    def setGameOver(self, bool):
        global gameOver
        if bool == True:
            gameOver = True
        if bool == False:
            gameOver = False

    def readCommand(self):
        global inputLine
        global inputHelper
        north = ['up', 'north', 'n'] #north
        south = ['down', 'south', 's'] #south
        east = ['east', 'e', 'right'] #est
        west = ['west', 'w', 'left'] #west
        go = ['move', 'walk', 'run', 'skip', 'hop', 'crawl', 'scoot', 'wander', 'meander', 'go'] #go

        look = ['look', 'see', 'peer', 'view'] #examine
        get = ['grab', 'get', 'take'] #get
        put = ['put', 'set', 'lay'] #put

        eat = ['eat'] # Player eats
        feed = ['feed'] # -> Gives food
        inventory = ['inventory']



        #Shortcut checks & Dictionary breakdown
        inputLine = input("")
        if inputLine in north:
            inputLine = "go north"
        elif inputLine in south:
            inputLine = "go south"
        elif inputLine in east:
            inputLine = "go east"
        elif inputLine in west:
            inputLine = "go west"
        elif (inputLine[0:2] in go or inputLine[0:3] in go or inputLine[0:4] in go or inputLine[0:5] in go) and (len(inputLine) < 6):
            inputLine = "go"
        elif inputLine[0:3] in put:
            inputHelper = inputLine[4:len(inputLine)]
            inputLine = "put"
        elif inputLine[0:3] in get:
            inputHelper = inputLine[4:len(inputLine)]
            inputLine = "get"
        elif inputLine[0:4] in get:
            inputHelper = inputLine[5:len(inputLine)]
            inputLine = "get"
        elif inputLine[0:3] in look:
            inputHelper = inputLine[4:len(inputLine)]
            inputLine = "look"
        elif inputLine[0:4] in look:
            inputHelper = inputLine[5:len(inputLine)]
            inputLine = "look"
        elif inputLine[0:3] in eat:
            inputHelper = inputLine[4:len(inputLine)]
            inputLine = "eat"
        elif inputLine[0:4] in feed:
            inputHelper = inputLine[5:len(inputLine)]
            inputLine = "feed"
        elif inputLine in inventory:
            inputLine = "inventory"

    def executeCommand(self):
        global gameOver
        global inputLine
        global inputHelper
        global health
        global playerInventory
        #print(inputLine[0:2] + "   " + inputLine[3:8]) #Debugging
        if inputLine == "exit":
            print("Bye!")
            gameOver = True
        elif inputLine[0:8] == "go north":
            Room1Printing.print_move("room 1", "north")
        elif inputLine[0:8] == "go south":
            Room1Printing.print_move("room 1", "south")
        elif inputLine[0:7] == "go east":
            Room1Printing.print_move("room 1", "east")
        elif inputLine[0:7] == "go west":
            Room1Printing.print_move("room 1", "west")
        elif inputLine == "go":
            print("Go where?")
        elif inputLine == "look":
            Room1Printing.print_look("room 1", inputHelper)
            if inputHelper != "north" and inputHelper != "south" and inputHelper != "west" and inputHelper != "east":
                Room1Printing.print_examine(inputHelper)
        elif inputLine == "get":
            print("Command "+inputLine)
            print("Object "+inputHelper)
            Room1Printing.print_get(inputHelper)
            playerInventory.append(inputHelper)
        elif inputLine == "put":
            print("Command "+inputLine)
            print("Object "+inputHelper)
        elif inputLine == "eat":
            print("Command "+inputLine)
            print("Object "+inputHelper)
            Room1Printing.print_eat_food(inputHelper)
        elif inputLine == "feed":
            print("Command "+inputLine)
            print("Object "+inputHelper)
            Room1Printing.print_feed_creature(inputHelper)
        elif inputLine == "inventory":
            Room1Printing.print_inventory(playerInventory)
        else:
            print("Invalid Command!")