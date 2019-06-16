from yamlreader import YamlReader
from mazeroom import MazeRoom 

class ValidMaze():

    actual_maze = []
    room_names = []
    room_cardinals = []
    valid_cardinals= (['north', 'east', 'south', 'west'])

    def load_maze(self):

        reader = YamlReader()
        maze   = reader.valid_path()

        ValidMaze.load_rooms(self,maze)
        ValidMaze.load_cardinals(self,maze)

    def load_rooms(self, maze):

        for room_name in maze:
            ValidMaze.room_names = list(maze[room_name].keys())

    def load_cardinals(self,maze):

        for room_name in maze:
             ValidMaze.room_cardinals = list(maze[room_name].values())

    def check_rooms(self):

        if len(ValidMaze.room_names) == 0:
            empty_maze = True
        else:
            empty_maze = False

        null_rooms  = None in ValidMaze.room_names
        empty_names = ""   in ValidMaze.room_names
        repeated_names = not len(set(ValidMaze.room_names)) == len(ValidMaze.room_names)
        
        invalid_rooms = empty_maze or null_rooms or empty_names or repeated_names

        return invalid_rooms

    def check_cardinals (self):

        invalid_cardinal = False

        for i in range(len(ValidMaze.room_cardinals)):
            
            if not (list(ValidMaze.room_cardinals[i].keys()) == ValidMaze.valid_cardinals):
                invalid_cardinal = True
                break
            else:
                continue
            
        return invalid_cardinal
    
    def check_dual_pointer (self):

        dual_pointer= False
  
        for i in range(len(ValidMaze.room_cardinals)):

            adjacent_rooms = list(ValidMaze.room_cardinals[i].values())
            adjacent_rooms [:] = (room for room in adjacent_rooms if room != None ) 
            unique_rooms = set(adjacent_rooms)
            if not ((len(adjacent_rooms) == len(unique_rooms))):
                dual_pointer = False
                break
            else:
                continue

        return dual_pointer

    def maze_assembly(self):

        for i in range(len(ValidMaze.room_names)):
            room = MazeRoom( ValidMaze.room_names[i],
                            ValidMaze.room_cardinals[i]['north'], 
                            ValidMaze.room_cardinals[i]['east'],
                            ValidMaze.room_cardinals[i]['south'],
                            ValidMaze.room_cardinals[i]['west'])
            ValidMaze.actual_maze.append(room)

    def print_actual_maze(self):

        print('\n')
        print('The rooms are: \n')

        for i in range(len(ValidMaze.actual_maze)):
            print('>' + ValidMaze.actual_maze[i].name )  
        
        print ('\n')
        
        
        for i in range(len(ValidMaze.actual_maze)):
            print (ValidMaze.actual_maze[i].name + ' is adjacent to: ')
            print ('>North: ')
            print (ValidMaze.actual_maze[i].north)
            print ('>East: ')
            print (ValidMaze.actual_maze[i].east)
            print ('>South:' )
            print (ValidMaze.actual_maze[i].south)
            print ('>West: ')
            print (ValidMaze.actual_maze[i].west)
            print ('\n \n' )
           
if __name__ == "__main__":  
   
    maze = ValidMaze()
    maze.load_maze()
    
    maze.maze_assembly()
    maze.print_actual_maze()
    
    
