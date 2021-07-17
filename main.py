import time

from conway import Conway_Abstract_Print as cb


begin = cb(5)

begin.create_grid()

while True:
    begin.print_grid()
    begin.print_grid_abstract()
    begin.grid_update()

    time.sleep(2)
