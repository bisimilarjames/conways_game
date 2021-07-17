import time

from conway import Conway_Abstract_Print as cb


begin = cb(10,0)

begin.create_grid()

while True:
    begin.print_dead_alive()
    begin.grid_update()

    time.sleep(2)
