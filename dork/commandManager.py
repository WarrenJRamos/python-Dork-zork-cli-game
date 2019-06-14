#Command keyword arrays
import sys
class CommandManager:

    inputLine = ""
    gameOver = False

    def start():
        print("Welcome to Dork!")
        print("You are in a dark room")
        global gameOver
        global inputLine
        gameOver = False

    def checkGameOver():
        global gameOver
        if gameOver == True:
            return True
        else:
            return False

    def readCommand():
        global inputLine
        north = ['up', 'north', 'n'] #north
        south = ['down', 'south', 's'] #south
        east = ['east', 'e', 'right'] #est
        west = ['west', 'w', 'left'] #west
        go = ['move', 'walk', 'run', 'skip', 'hop', 'crawl', 'scoot', 'wander', 'meander', 'go'] #go

        look = ['examine', 'look', 'see', 'peer', 'view'] #examine
        get = ['grab', 'pick up', 'get', 'take'] #get
        put = ['put', 'set', 'lay'] #put

        inputLine = input("")
        if inputLine in north:
            inputLine = "go north"
        elif inputLine in south:
            inputLine = "go south"
        elif inputLine in east:
            inputLine = "go east"
        elif inputLine in west:
            inputLine = "go west"
        elif inputLine[0:2] in go or inputLine[0:3] or inputLine[0:4] or inputLine[0:5]:
            inputLine = "go"
        elif inputLine in look:
            inputLine = "examine"
        elif inputLine in get:
            inputLine = "grab"
        elif inputLine in put:
            inputLine = "put"


    def executeCommand():
        global gameOver
        global inputLine
        print(inputLine[0:2] + "   " + inputLine[3:8]) #Debugging
        if inputLine == "exit":
            print("Bye!")
            gameOver = True
            pass
        elif inputLine[0:8] == "go north":
            print("You went North!")
            pass
        elif inputLine[0:8] == "go south":
            print("You went South!")
            pass
        elif inputLine[0:7] == "go east":
            print("You went East!")
            pass
        elif inputLine[0:7] == "go west":
            print("You went West!")
            pass
        elif inputLine == "go":
            print("Go where")
            pass
        else:
            print("Invalid Command!")
            
    def enterRoom():
        return