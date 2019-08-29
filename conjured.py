class Conjured:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.quality > 0:
            if self.sell_in > 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 4
