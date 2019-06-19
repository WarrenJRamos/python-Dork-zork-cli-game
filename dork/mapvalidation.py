"""
A class that validates a maze coming from a .yml/.yaml file
"""
from dork.mazeroom import MazeRoom

class ValidMaze():
    """
    A valid maze
    """
    actual_maze = []
    room_names = []
    room_cardinals = []
    valid_cardinals = ['north', 'east', 'south', 'west']
    
    def load_rooms(self, maze):
        """
        Loading the room names
        """
        for room_name in maze:
            ValidMaze.room_names = list(maze[room_name].keys())
    
    def load_cardinals(self, maze):
        """
        Loading the room cardinals
        """
        for room_name in maze:
            ValidMaze.room_cardinals = list(maze[room_name].values())

    def check_rooms(self):
        """
        Checking room names for valid names
        """
        return None in ValidMaze.room_names

    def check_cardinals(self):
        """
        Checking for valid cardinals in each room
        """
        invalid_cardinal = False

        for i in range(len(ValidMaze.room_cardinals)):
            if  list(ValidMaze.room_cardinals[i].keys()) != ValidMaze.valid_cardinals:
                invalid_cardinal = True
                break
            else:
                continue
        return invalid_cardinal
    def check_connections(self):
        """
        Checking for cardinals to be pointing to unique and valid directions
        """
        dual_pointer = False
        invalid_direction = False
        isolated_room = False
        for i in range(len(ValidMaze.room_cardinals)):

            adjacent_rooms = list(ValidMaze.room_cardinals[i].values())
            adjacent_rooms [:] = (room for room in adjacent_rooms if room is not None)
            unique_rooms = set(adjacent_rooms)
            if len(adjacent_rooms) != len(unique_rooms):
                dual_pointer = True
                break
            elif not set(adjacent_rooms).issubset(set(ValidMaze.room_names)):
                invalid_direction = True
                break
            elif unique_rooms.issubset({None}):
                isolated_room = True
                break
            else:
                continue

        return dual_pointer or invalid_direction or isolated_room

    def maze_assembly(self):
        """
        Appending rooms to the maze
        """

        for i in range(len(ValidMaze.room_names)):
            room = MazeRoom(ValidMaze.room_names[i],
                            ValidMaze.room_cardinals[i]['north'],
                            ValidMaze.room_cardinals[i]['east'],
                            ValidMaze.room_cardinals[i]['south'],
                            ValidMaze.room_cardinals[i]['west'])
            ValidMaze.actual_maze.append(room)

    def print_actual_maze(self):
        """
        Printing the maze
        """

        print('\n')
        print('The rooms are: \n')

        for i in range(len(ValidMaze.actual_maze)):
            print('>' + ValidMaze.actual_maze[i].name)
        print('\n')
        for i in range(len(ValidMaze.actual_maze)):
            print(ValidMaze.actual_maze[i].name + ' is adjacent to: ')
            print('>North:')
            print(ValidMaze.actual_maze[i].north)
            print('>East:')
            print(ValidMaze.actual_maze[i].east)
            print('>South:')
            print(ValidMaze.actual_maze[i].south)
            print('>West:')
            print(ValidMaze.actual_maze[i].west)
            print('\n \n')
