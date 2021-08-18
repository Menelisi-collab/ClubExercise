# MainCode
from ClubPack.Players import Players
from ClubPack.Drivers import Driver
from ClubPack.Bus import Bus
from ClubPack import Coaches
from ClubPack import Physios
from ClubPack import BoardMembers
from ClubPack import Fans


player1 = Players("Diego", "Alvares", 25, "Midfielder", 2018-2023)
player2 = Players("Melusi", "Simelane", 30, "Striker", 2012-2024)
player3 = Players("John", "Colson", 24, "Right_Fullback", 2020-2025)

bus_01 = Bus(brand="Benz", seat_count=24)
driver_01 = Driver(driver_status=False, driver_name="Menelisi", bus_type=bus_01 , driver_licence='Code36')
driver_02 = Driver(bus_type="Man", driver_name="Will Smith", driver_status=False, driver_licence='Code1')


print(driver_02.bus_type)
bus_01.theName()
print(driver_01.bus_type)
