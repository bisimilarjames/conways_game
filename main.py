import time

from features import Conway_Alternative_Grids as cag

test = cag(5,5)

test.create_grid()
test.print_grid()


while True:
    test.print_grid_abstract(True)
    test.print_dead_alive()
    test.cylinder_update()
#    test.print_grid()

    time.sleep(2)
