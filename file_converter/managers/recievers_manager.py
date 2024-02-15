class RecieverManager:
    def __init__(self):
        self._recievers = {}

    
    def register(self, format, reciever):
        self._recievers[format] = reciever
    

    def get(self, format, input_):
        reciever = self._recievers[format]
        if not reciever:
            raise ValueError(f"{format} format isn't registered.")
        return reciever(input_)
    

recievers_manager = RecieverManager()
recievers = recievers_manager._recievers