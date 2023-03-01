from turtle import Turtle

# SETTINGS
STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake():
    """Models a Snake that represents the player in the Snake Game"""

    def __init__(self):
        '''Creates an snake'''
        self.segments = []
        self.createSnake()


    def createSnake(self):
        '''Generates the first three segments of a Snake'''
        for pos in STARTING_POS:
            new_segment = Turtle()
            new_segment. shape('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
          
    
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)