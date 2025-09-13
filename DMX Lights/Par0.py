from DMXLight import DMXLight

class Par0(DMXLight):
    def __init__(self, node, universe: int, start_channel: int):
        super().__init__(node, universe, start_channel, 5)

    def setFade(self, fade: int = 0, timespan: float = 0):
        self.setFixture(0, fade, timespan)

    def setColor(self, red: int = None, green: int = None, blue: int = None, white: int = None, timespan: float = 0):
        if red: self.setFixture(1, red, timespan)
        if green: self.setFixture(2, green, timespan)
        if blue: self.setFixture(3, blue, timespan)
        if white: self.setFixture(4, white, timespan)

    def blackout(self):
        self.reset()