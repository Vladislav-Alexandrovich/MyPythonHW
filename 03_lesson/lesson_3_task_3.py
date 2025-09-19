from mailing import Mailing
from address import Address

from_address = Address(100000, "Moscow", "Мира", 10, 45)
to_address = Address(188100, "Saint-Petersburg", "Счастья", 20, 50)

mailing = Mailing(from_address, to_address, 500, 12345)

print(to_address)
print(mailing)

