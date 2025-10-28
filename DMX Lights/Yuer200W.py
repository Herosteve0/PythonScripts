from DMXLight import DMXLight

class Yuer200W(DMXLight):
    def __init__(self, dmxhub, start_channel: int):
        super().__init__(dmxhub, start_channel, 15)

    def setDimmer(self, dimmer: int = 0):
        self.setFixture(6, dimmer)

    def setColor(self, red: int = None, green: int = None, blue: int = None, white: int = None):
        if red: self.setFixture(2, red)
        if green: self.setFixture(3, green)
        if blue: self.setFixture(4, blue)
        if white: self.setFixture(5, white)

    def setStrobo(self, value: int = None):
        self.setFixture(7, value)

    def blackout(self):
        self.reset()