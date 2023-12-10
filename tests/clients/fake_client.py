class FakeClient:
    def __init__(self, text) -> None:
        self.text = text

    def get(self, url):
        if self.text == 'Failure':
            raise Exception
        return self