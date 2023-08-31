from mailing import mailing
from address import address

senderAddress = address(617700, 'Куеда', 'улица Коммунальная', 29, 1)
recieverAddress = address(108849, 'Москва', 'улица Самуила Маршака', 12, 62)

newMailing = mailing(senderAddress, recieverAddress, 1795, '88003356416842122')

print('Отправление ', end = '')
newMailing.trackId()
print(' из', end = ' ')

senderAddress.indexId()
senderAddress.nameCity()
senderAddress.nameStreet()
senderAddress.numBuilding()
senderAddress.numApart()
print(end = ' ')

print('в', end = ' ')
recieverAddress.indexId()
recieverAddress.nameCity()
recieverAddress.nameStreet()
recieverAddress.numBuilding()
recieverAddress.numApart()
print(end = '. ')

newMailing.price()