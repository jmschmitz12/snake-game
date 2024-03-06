from segment import Segment


class Snake:
    """list of snake segments including head and body"""
    def __init__(self):
        self.segments = []
        for x in [0, -20, -40]:
            segment = Segment(x, 0)
            self.segments.append(segment)
        self.head = self.segments[0]
        self.body = self.segments[1:]

    def move_right(self):
        next_x_position = self.head.x
        next_y_position = self.head.y

        self.head.x += 20
        self.head.update()

        self.body_update(next_x_position, next_y_position)

    def move_left(self):
        next_x_position = self.head.x
        next_y_position = self.head.y

        self.head.x -= 20
        self.head.update()

        self.body_update(next_x_position, next_y_position)

    def move_up(self):
        next_x_position = self.head.x
        next_y_position = self.head.y

        self.head.y += 20
        self.head.update()

        self.body_update(next_x_position, next_y_position)

    def move_down(self):
        next_x_position = self.head.x
        next_y_position = self.head.y

        self.head.y -= 20
        self.head.update()

        self.body_update(next_x_position, next_y_position)

    def body_update(self, next_x_position, next_y_position):
        """Iterates through the body segments of the snake and updates the x, y positions"""
        for segment in self.body:
            current_x_position = segment.x
            current_y_position = segment.y

            segment.x = next_x_position
            segment.y = next_y_position
            segment.update()

            next_x_position = current_x_position
            next_y_position = current_y_position

    def add_segment(self):
        # Get the last segment's position
        last_segment = self.body[-1]
        new_x = last_segment.x
        new_y = last_segment.y

        # Create a new segment at this position (you might want to adjust this logic based on your game's design)
        new_segment = Segment(new_x, new_y)

        # Append the new segment to the body
        self.body.append(new_segment)

    def did_collide(self):
        for segment in self.body:
            if self.head.x == segment.x and self.head.y == segment.y:
                return True
        return False






