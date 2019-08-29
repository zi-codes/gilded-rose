class Item:

    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.quality < 50:
            if self.quality > 0:
                self.quality -= self.decrement()

    def decrement(self):
        return 1 if self.sell_in > 0 else 2
