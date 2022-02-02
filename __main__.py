import time
from ballon import Ballon
from clown import Clown

def current_time_ms():
    return round(time.time() * 1000)



print(current_time_ms())
first_ballon = Clown.buy_ballon(3)
second_ballon = Clown.buy_ballon(3)
ballon_list = []
for i in range(10):
    ballon_list.append(Clown.buy_ballon(3))

first_ballon.update(current_time_ms())
first_ballon.pop()

for ballon in ballon_list:
    print(ballon)
