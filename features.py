from input import Life_and_Death_rules as ld

class Conway_Abstract_Print(ld):
    "A Class with a function that only prints the alive squares"

    def print_grid_abstract(self, swi):
        """
        Prints out the grid as several strings of only alive states.
        Alive states are an X alive states.
        Dead states are left blank

        data input: Life and death switch (Bool), the number of rows (int), the grid storage list
        data output:n/a
        """
        #####Declerations#####

        #####Computations#####
        #Loops through each row in the grid
        for i in range(self.row):
            #Identifies the currently alive states in this iteration of the grid
            #Prints out the alive states of the current row
            print(self.string_creation(self.find_alive(i),swi))

        #New line to seperate the grids in the terminal
        print('\n')


    def print_dead_alive(self):
        """
        Prints the alive and dead abstract grids next to each other.

        data input: The number of rows (int), the grid storage list
        data output: n/a
        """
        #####Declerations#####
        ####Data Structure####
        alive = []

        #####Computations#####
        #Loops through each row in the grid
        for i in range(self.row):
            #Identifies the currently alive states in this iteration of the grid
            alive = self.find_alive(i)
            #Prints out the alive states of the current row
            print(self.string_creation(alive,True) + '\t' + self.string_creation(alive,False))

        #New line to seperate the grids in the terminal
        print('\n')


    def find_alive(self, index):
        """
        Finds the alive states in the current row

        data input: The number of rows & columns (int), the grid storage list, the current row index (int)
        data output: A list with the (int) indicies of the elements in the current row that are alive
        """
        #####Declerations#####

        #####Computations#####
        #Returns the alive states by
        #looping through each element in the row and checks if it is alive or dead
        return [a for a, value in enumerate(self.grid[0 + self.col * index : self.col * (1 + index)]) if value == 1]



    def string_creation(self, aliveness, daswi):
        """
        Creates the string version of the current row that has been searched for alive states

        data input: The number of columns (int), the dead or alive switch (Bool), the list that stores the indicies of the alive states in the current row (int)
        data output: A string with either all the alive element positions set to 'X' or
        the dead element positions set to 'O'
        """
        #####Declerations#####
        ####Variables####
        printout = ''

        #####Computations#####
        #If the user wants to print the alive states
        if daswi == True:
            printstore = ['X ' if x in aliveness else '  ' for x in range(self.col)]
        #If the user wants to print the death states
        elif daswi == False:
            printstore = [' ' if x in aliveness else 'O ' for x in range(self.col)]

        #Returns the row as a string
        return(printout.join(printstore))
