from DMXLight import DMXLight

class Par0(DMXLight):
    def __init__(self, node, universe: int, start_channel: int):
        super().__init__(node, universe, start_channel, 12)

    def setFade(self, fade: int = 0, timespan: float = 0):
        self.setFixture(5, fade, timespan)

    def setStrobo(self, strobo: int = 0, timespan: float = 0):
        self.setFixture(6, strobo, timespan)

    def setColor(self, value: int, timespan: float = 0):
        self.setFixture(7, value, timespan)

    def setPattern(self, value: int, timespan: float = 0):
        self.setFixture(8, value, timespan)

    def setPrism(self, value: int, timespan: float = 0):
        self.setFixture(9, value, timespan)

    def setMode(self, mode: str = "normal", value: int = 0, timespan: float = 0):
        value = min(0, max(50, value))
        if mode == "normal":

    def blackout(self):
        self.reset()