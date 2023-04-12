from tire.tire import Tire


class Carrigane(Tire):
    def __init__(self, data):
        super().__init__(data)

    def needs_service(self):
        for d in self.data:
            if d >= 0.9:
                return True
        return False