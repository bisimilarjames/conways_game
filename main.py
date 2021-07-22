import time

#from features import Conway_Abstract_Print as cap
from features import Conway_Abstract_Print as ca
from features import Conway_Input as ci

test = ca(10,5)


test.create_grid()
test.print_grid()

while True:
    #begin.print_grid_abstract(True)
    test.print_dead_alive()
    test.grid_update()

    time.sleep(2)
