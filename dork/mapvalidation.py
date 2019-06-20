"""
A class that validates a maze coming from a .yml/.yaml file
"""
class ValidMaze:
    """
    A valid maze
    """
    @classmethod
    def load_rooms(cls, maze):
        """
        Loading the room names
        """
        for room_name in maze:
            room_names = list(maze[room_name].keys())
        return room_names
    @classmethod
    def load_cardinals(cls, maze):
        """
        Loading the room cardinals
        """
        for room_name in maze:
            room_cardinals = list(maze[room_name].values())
        return room_cardinals
    @classmethod
    def check_rooms(cls, room_names):
        """
        Checking room names for valid names
        """
        return None in room_names
    @classmethod
    def check_cardinals(cls, room_cardinals):
        """
        Checking for valid cardinals in each room
        """
        valid_cardinals = ['north', 'east', 'south', 'west']
        invalid_cardinal = False

        for i in enumerate(len(room_cardinals)):
            if  list(room_cardinals[i].keys()) != valid_cardinals:
                invalid_cardinal = True
                break
        return invalid_cardinal
    @classmethod
    def check_connections(cls, room_names, room_cardinals):
        """
        Checking for cardinals to be pointing to unique and valid directions
        """
        dual_pointer = False
        invalid_direction = False
        isolated_room = False
        for i in enumerate(len(room_cardinals)):

            adjacent_rooms = list(room_cardinals[i].values())
            adjacent_rooms [:] = (room for room in adjacent_rooms if room is not None)
            unique_rooms = set(adjacent_rooms)
            if len(adjacent_rooms) != len(unique_rooms):
                dual_pointer = True
                break
            elif not set(adjacent_rooms).issubset(set(room_names)):
                invalid_direction = True
                break
            elif unique_rooms.issubset({None}):
                isolated_room = True
                break
        return dual_pointer or invalid_direction or isolated_room
    @classmethod
    def print_actual_maze(cls, room_names, room_cardinals):
        """
        Printing the maze
        """
        print('\n')
        print('The rooms are: \n')

        for i in enumerate(room_names):
            print('>' + room_names[i])
        print('\n')
        for i in enumerate(room_names):
            print(room_names[i] + ' is adjacent to: ')
            print('>North:')
            print(room_cardinals[i]['north'])
            print('>East:')
            print(room_cardinals[i]['east'])
            print('>South:')
            print(room_cardinals[i]['west'])
            print('>West:')
            print(room_cardinals[i]['south'])
            print('\n \n')
    