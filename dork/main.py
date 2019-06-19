"""
Main Method
"""
import yaml
from dork.mapvalidation import ValidMaze
from dork.yamlreader import YamlReader

if __name__ == "__main__":
    VALID_MAZE = ValidMaze()
    READER = YamlReader()
    VALIDATED = True
    while VALIDATED:
        try:
            MAZE_DATA = READER.valid_path_file()
            VALID_MAZE.load_rooms(MAZE_DATA)
            INVALID_ROOMS = VALID_MAZE.check_rooms()
            VALID_MAZE.load_cardinals(MAZE_DATA)
            INVALID_CONNECTIONS = VALID_MAZE.check_cardinals() or VALID_MAZE.check_connections()
        except (TypeError, AttributeError, yaml.parser.ParserError):
            print('\nPlease provide a file that contains a well formatted non-empty maze.\n')
        else:
            if INVALID_ROOMS:
                print('\nThe maze can not have empty or null names for the rooms.\n')
            elif INVALID_CONNECTIONS:
                print('\nPlease assure that the uploaded maze fulfills these conditions:')
                print('\nThe maze must have the cardinal names for the rooms as follow:')
                print(ValidMaze.valid_cardinals)
                print('\nThe cardinals in the rooms must be pointing to unique directions.\n')
                print('\nThe cardinals in the rooms can not point to rooms out of the maze.\n')
                print('\nThere are not unreachable rooms in the maze.\n')
            else:
                VALIDATED = False
                print('The maze provided by the user has been uploaded successfully.')
    VALID_MAZE.maze_assembly()
    VALID_MAZE.print_actual_maze()
    