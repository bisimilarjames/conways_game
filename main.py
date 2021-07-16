import time

from conway import Conway_Base as con


begin = con(10)

begin.create_grid()

while True:
    begin.print_grid()
    begin.grid_update()

    time.sleep(2)
