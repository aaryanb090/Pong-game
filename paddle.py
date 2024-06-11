from turtle import Turtle
INITIAL_POS = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        current_pos = self.pos()
        current_y = current_pos[1]
        current_x = current_pos[0]
        self.goto(x=current_x, y=current_y + 20)

    def down(self):
        current_pos = self.pos()
        current_y = current_pos[1]
        current_x = current_pos[0]
        self.goto(x=current_x, y=current_y - 20)
