import time

from features import Conway_Alternative_Grids as cag

test = cag(4,4)

test.create_grid()
test.print_grid()
#test.grid_update()
#test.periodic_grid_update()
test.wrap_round_update()
#test.cylinder_update()
test.print_grid()


#while True:
#    test.print_grid_abstract(True)
#    test.print_dead_alive()
#    test.grid_update()
#    test.print_grid()

#    time.sleep(2)
