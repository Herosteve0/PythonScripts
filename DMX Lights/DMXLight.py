class DMXLight:
    def __init__(self, dmxhub, start_channel: int, fixtures: int):
        self.dmxhub = dmxhub
        self.start_channel = start_channel
        self.fixtures_length = fixtures

    def setFixture(self, fixture: int, value: int):
        self.dmxhub.set_channel(self.start_channel + fixture - 1, value)

    def reset(self):
        for i in range(self.fixtures_length):
            self.dmxhub.set_channel(i, 0)