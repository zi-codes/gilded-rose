class BackstagePass:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.quality > 0:
            if self.quality < 50:
                if self.sell_in > 10:
                    self.quality = self.quality + 1
                elif self.sell_in > 5:
                    self.quality = self.quality + 2
                elif self.sell_in >= 0:
                    self.quality = self.quality + 3
                else:
                    self.quality = 0
