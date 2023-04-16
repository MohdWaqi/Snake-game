from turtle import Turtle

STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

############################## Creating the body of the snake ###########################

    def create_snake(self):
        for position in STARTING_POINT:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self):
        for piece in self.segment:
            piece.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for piece in range(len(self.segment) - 1, 0, -1):
            new_x_coordinates = self.segment[piece - 1].xcor()
            new_y_coordinates = self.segment[piece - 1].ycor()
            self.segment[piece].goto(new_x_coordinates, new_y_coordinates)

        self.head.forward(MOVE_DISTANCE)

#################################### Movement of the snake #############################################

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
