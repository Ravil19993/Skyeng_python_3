class address():

    def __init__(self, index, city, street, building, apart):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apart = apart

    def indexId(self):
        print(self.index, end = ', ')

    def nameCity(self):
        print(self.city, end = ', ')

    def nameStreet(self):
        print(self.street, end = ', ')

    def numBuilding(self):
        print(self.building, end = ' - ')

    def numApart(self):
        print(self.apart, end = '')