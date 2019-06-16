"""
A class that models the behaviour of a room
"""
class MazeRoom():
    """
    A room.
    """
    def __init__(self, name, north, east, south, west):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
