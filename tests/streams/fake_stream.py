class FakeStream:
    def __init__(self, input):
        self.input = input

    def read(self):
        return self.input