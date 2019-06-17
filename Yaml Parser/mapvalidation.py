"""
A class that validates a maze coming from a .yml/.yaml file
"""
import yaml
from yamlreader import YamlReader
from mazeroom import MazeRoom

class ValidMaze():
    """
    A valid maze
    """
    actual_maze = []
    room_names = []
    room_cardinals = []
    valid_cardinals = (['north', 'east', 'south', 'west'])
    def load_valid_maze(self):
        """
        Validating and loading the maze
        """

        reader = YamlReader()
        validated = True
        while validated:
            try:
                maze = reader.valid_path_file()
                ValidMaze.load_rooms(self, maze)
                invalid_rooms = ValidMaze.check_rooms(self)
                ValidMaze.load_cardinals(self, maze)
                invalid_connections = ValidMaze.check_connections(self)
            except (TypeError, AttributeError, yaml.parser.ParserError):
                print('\nPlease provide a file that contains a well formatted non-empty maze.\n')
            else:
                if invalid_rooms:
                    print('\nThe maze can not have empty or null names for the rooms.\n')
                elif invalid_connections:
                    print('\nPlease assure that the uploaded maze fulfills these conditions:')
                    print('\nThe maze must have the cardinal names for the rooms as follow:')
                    print(ValidMaze.valid_cardinals)
                    print('\nThe cardinals in the rooms must be pointing to unique directions.\n')
                    print('\nThe cardinals in the rooms can not point to rooms out of the maze.\n')
                    print('\nThere are not unreachable rooms in the maze.\n')
                else:
                    validated = False
                    print('The maze provided by the user has been uploaded successfully.')

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
            if list(ValidMaze.room_cardinals[i].keys()) != ValidMaze.valid_cardinals:
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
            if not len(adjacent_rooms) == len(unique_rooms):
                dual_pointer = True
                break
            elif not set(adjacent_rooms).issubset(set(ValidMaze.room_names)):
                invalid_direction = True
                break
            elif set(adjacent_rooms).issubset({None}):
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

if __name__ == "__main__":
    MAZE_1 = ValidMaze()

    MAZE_1.load_valid_maze()
    MAZE_1.maze_assembly()
    MAZE_1.print_actual_maze()
    