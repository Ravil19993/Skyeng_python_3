from smartphone import smartphone

catalog = [
    smartphone("Nokia - ", "3600, ", "+7(902) 795-12-26"),
    smartphone('Motorola - ', 'Razor, ', '+7(950) 113-12-66'),
    smartphone('iPhone - ', '12, ', '+7(982) 448-48-11'),
    smartphone('Samsung - ', 'A +, ', '+7(962) 888-22-33'),
    smartphone('Xiaomi - ', 'V +. ', '+7(999) 444-66-82')
]

for X in range (0, len(catalog)):
    phone = catalog[X]
    phone.typ()
    phone.model()
    phone.number()