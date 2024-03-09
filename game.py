from turtle import Screen
from snake import Snake
from target import Target
import time

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')

        self.screen.tracer(0, 0)  # Disable automatic screen updates

        self.score = 0
        self.screen.title(f"Snake Game, Score: {self.score}")

        self.snake = Snake()
        self.target = Target()
        self.target.update()
        self.active_direction = None
        self.active_game = True

        self.screen.listen()
        self.screen.onkey(self.set_direction_right, "Right")
        self.screen.onkey(self.set_direction_left, "Left")
        self.screen.onkey(self.set_direction_up, "Up")
        self.screen.onkey(self.set_direction_down, "Down")

        self.game_loop()

    def game_loop(self):
        while self.active_game:
            self.screen.update()  # Manually update the screen
            time.sleep(0.06)  # Control the refresh rate

            # Move the snake based on the current direction
            if self.active_direction == "Right":
                self.snake.move_right()
            elif self.active_direction == "Left":
                self.snake.move_left()
            elif self.active_direction == "Up":
                self.snake.move_up()
            elif self.active_direction == "Down":
                self.snake.move_down()

            self.evaluate_boundaries()
            self.evaluate_collisions()
            self.evaluate_target()

    def set_direction_right(self):
        self.active_direction = "Right"

    def set_direction_left(self):
        self.active_direction = "Left"

    def set_direction_up(self):
        self.active_direction = "Up"

    def set_direction_down(self):
        self.active_direction = "Down"

    def evaluate_target(self):
        # Assuming target.update() refreshes the target's position and snake.add_segment() adds a new segment properly
        if self.target.x == self.snake.head.x and self.target.y == self.snake.head.y:
            self.score += 1
            self.target.update()
            self.snake.add_segment()
            self.screen.title(f"Snake Game, Score: {self.score}")

    def evaluate_boundaries(self):
        if self.snake.head.x > 280 or self.snake.head.x < -280 or self.snake.head.y > 280 or self.snake.head.y < -280:
            self.end_game()


    def evaluate_collisions(self):
        if self.snake.did_collide():
            self.end_game()


    def end_game(self):
        self.active_game = False
        print(f"Game over! Score is {self.score}")
