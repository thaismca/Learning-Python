from turtle import Turtle
from settings import SHAPE_STRETCH

# Snake settings
STARTING_POS = [(0,0), (-20 * SHAPE_STRETCH,0), (-40 * SHAPE_STRETCH,0)]
MOVE_DISTANCE = 20 * SHAPE_STRETCH
# headings 
UP_NORTH = 90
LEFT_WEST = 180
DOWN_SOUTH = 270
RIGHT_EAST = 0

class Snake():
    """Models a Snake that represents the player in the Snake Game"""

    def __init__(self):
        '''Creates an snake'''
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]


    def createSnake(self):
        '''Generates the first three segments of a Snake'''
        for pos in STARTING_POS:
            self.add_segment(pos)
          
    
    def add_segment(self, position):
        """Adds a new segment to the given position"""
        new_segment = Turtle()
        new_segment. shape('square')
        new_segment.shapesize(SHAPE_STRETCH, SHAPE_STRETCH)
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        """Adds a new segment after the current last one"""
        last_seg_position = self.segments[-1].pos()
        self.add_segment(last_seg_position)

    
    def move(self):
        '''Moves the snake constantly forward at a given pace'''
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    
    def reset_snake(self):
        """Clear current snake segments and creates a new starting snake with three segments"""
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    
    def up(self):
        '''Turns the snake to north direction, if it's currently not going towards south'''
        if self.head.heading() != DOWN_SOUTH:
            self.head.setheading(UP_NORTH)

    
    def left(self):
        '''Turns the snake to west direction, if it's currently not going towards east'''
        if self.head.heading() != RIGHT_EAST:
            self.head.setheading(LEFT_WEST)

    
    def down(self):
        if self.segments[0].heading() != UP_NORTH:
            '''Turns the snake to south direction, if it's currently not going towards north'''
            self.segments[0].setheading(DOWN_SOUTH)

    def right(self):
        '''Turns the snake to east direction, if it's currently not going towards west'''
        if self.segments[0].heading() != LEFT_WEST:
            self.segments[0].setheading(RIGHT_EAST)