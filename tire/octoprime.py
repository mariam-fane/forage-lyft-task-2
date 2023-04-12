from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self, data):
        super().__init__(data)

    def needs_service(self):

        return sum(self.data) >= 3