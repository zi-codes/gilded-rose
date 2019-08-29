class Brie:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
