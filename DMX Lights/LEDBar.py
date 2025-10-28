from DMXLight import DMXLight

class LEDBar13(DMXLight):
    def __init__(self, dmxhub, start_channel: int):
        super().__init__(dmxhub, start_channel, 13)

    def setPosY(self, value: int, speed: int = 0):
        self.setFixture(2, speed)
        self.setFixture(1, value)

    def setDimmer(self, dimmer: int = 0):
        self.setFixture(3, dimmer)

    def setColor(self, red: int = None, green: int = None, blue: int = None, white: int = None):
        if red: self.setFixture(5, red)
        if green: self.setFixture(6, green)
        if blue: self.setFixture(7, blue)
        if white: self.setFixture(8, white)

    def setBackgroundColor(self, value: int = None, tone: int = None):
        if value: self.setFixture(11, value)
        if tone: self.setFixture(12, tone)

    def setStrobo(self, value: int = None):
        self.setFixture(4, value)

    def setPattern(self, value: int = None, speed: int = -127):
        speed = min(max(speed+127, 0), 255)
        self.setFixture(10, speed+127)
        self.setFixture(9, value*2)

    def blackout(self):
        self.reset()