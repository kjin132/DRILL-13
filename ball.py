from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    SMALL = 'small'
    LARGE = 'large'
    images = {}

    def __init__(self, x, y, velocity, ball_type=SMALL):
        if ball_type not in (self.SMALL, self.LARGE):
            raise ValueError(f'Unsupported ball type: {ball_type}')
        if ball_type not in Ball.images:
            filename = 'ball41x41.png' if ball_type == self.LARGE else 'ball21x21.png'
            Ball.images[ball_type] = load_image(filename)
        self.x, self.y = x, y
        self.velocity = velocity
        self.ball_type = ball_type

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        Ball.images[self.ball_type].draw(self.x, self.y)
