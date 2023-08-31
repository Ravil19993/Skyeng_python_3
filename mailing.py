from address import address

class mailing():
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def trackId(self):
        print(self.track, end = '')
    
    def reciever(self):
        print(self.to_address)

    def sender(self):
        print(self.from_address)

    def price(self):
        print('Стоимость', self.cost, 'рублей.')
