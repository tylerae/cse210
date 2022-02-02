from tank import Tank 
from ballon import Ballon

class Clown:
    def __init__(self):
        self.tank = Tank("Heluim")
        self.money = 0 
        

    def buy_ballon(self, cost):
        ballon = Ballon("Red")
        ballon.fill(self.tank.release_air(500))
        self.moeny += cost 
        return ballon

