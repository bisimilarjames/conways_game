import time

from features import Conway_Abstract_Print as cap

test = cap(4,4)

test.create_grid()

test.print_grid()
test.grid = [1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1]
test.print_grid()

#while True:
#    test.print_grid_abstract(True)
#    test.print_dead_alive()
#    test.grid_update()
#    test.print_grid()

#    time.sleep(2)
