from DMXLight import DMXLight

class KingPar3(DMXLight):
    def __init__(self, dmxhub, start_channel: int):
        super().__init__(dmxhub, start_channel, 7)

    def setDimmer(self, dimmer: int = 0):
        self.setFixture(1, dimmer)

    def setColor(self, red: int = None, green: int = None, blue: int = None, white: int = None):
        if red: self.setFixture(2, red)
        if green: self.setFixture(3, green)
        if blue: self.setFixture(4, blue)
        if white: self.setFixture(5, white)

    def setStrobo(self, value: int = None):
        self.setFixture(6, value)

    def setFunction(self, value: int = None):
        if value == 1:
            v = 16
        elif value == 2:
            v = 38
        elif value == 3:
            v = 61
        elif value == 4:
            v = 84
        elif value == 5:
            v = 107
        elif value == 6:
            v = 130
        elif value == 7:
            v = 153
        elif value == 8:
            v = 176
        elif value == 9:
            v = 199
        elif value == 10:
            v = 222
        elif value == 11:
            v = 245
        else:
            if value: print(f"Unknown value given to {self} function ({value}), resetting function to 0.")
            v = 0
        self.setFixture(7, v)

    def blackout(self):
        self.reset()