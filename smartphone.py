class smartphone():

    def __init__(self, typ, model, phoneNumber):
        self.tip = typ
        self.mod = model
        self.num = phoneNumber

    def typ(self):
        print(self.tip, end = '')

    def model(self):
        print(self.mod, end = '')

    def number(self):
        print(self.num)