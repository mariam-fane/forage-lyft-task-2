from abc import ABC


class Tire(ABC):
    def __init__(self, data):
        self.data = data
    def needs_service(self):
        pass
