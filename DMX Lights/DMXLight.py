class DMXLight:
    def __init__(self, node, _universe: int, start_channel: int, fixtures: int):
        self.start_channel = start_channel

        universe = node.add_universe(_universe)
        self.fixtures = [
            universe.add_channel(start=start_channel+i+1, width=1) for i in range(fixtures)
            ]

    def setFixture(self, fixture: int, value: int, timespan: float = 0):
        self.fixtures[fixture].add_fade([value], timespan)

    def reset(self):
        for fixture in self.fixtures:
            fixture.add_fade([0], 0)