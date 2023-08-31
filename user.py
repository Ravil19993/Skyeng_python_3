class user():

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def sayName(self):
        print('Мое имя: ', self.name)

    def saySurname(self):
        print('Моя фамилия: ', self.surname)

    def sayFullName(self):
        print('Мое полное имя: ', self.name, self.surname)