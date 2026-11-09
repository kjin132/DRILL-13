from pico2d import load_image


class ItemMode:
    def __init__(self):
        self.active = False
        self.image = load_image('item_select.png')

    def toggle(self):
        self.active = not self.active

    def draw(self):
        if self.active:
            self.image.draw(400, 300)
