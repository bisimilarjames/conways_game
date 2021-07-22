from conway import Conway_Base as cb

class Conway_Input(cb):
    "A class whose initialisation allows for the generic arguments so a rectanglular grid can be constructed"

    def __init__(self,*args):
        """
        Initialises the class
        Takes the number of rows and columns in a generic argument
        Checks that the arg tuple is of length 1 or 2
        Checks the content of the tuple
        Allocates the method arguments to the number of rows and columns the grid will contain


        data input: One or two integer. First is for the number of rows. The second, if used, is for the number of columns
        data output: (int) Variables for the number of columns and rows the game of life grid will have
        """
        #####Declerations#####

        #####Computations#####
        #Checks the length of the argument tuple for the number of user inputs
        #If there is one user input
        if (len(args) == 1):
            #Checks the correctness of the input
            self.input_checker(args[0],True)
            #If the input is correct it passes it to an initialisation of the Conway_base class
            super().__init__(args[0])

        #If there are two user inputs
        elif (len(args) == 2):
            #Checks the inputs seperatley
            self.input_checker(args[0],True)
            self.input_checker(args[1],False)

            #Assigns the user input to the classes row and column variables
            self.row = args[0]
            self.col = args[1]

        #If the input tuple is any other length
        else:
            #Prints error and then quits the program
            print('Initialisat Method must have one or two integer inputs only')
            quit()

    def input_checker(self,ndim,sel):
        """
        Checks the initalised user input for the grid dimensions is type correct and mathematically possible
        Gives error message and quits the program if not

        data input:  A grid dimension (int) and a switch variable to select if it is a row or a column (bool)
        data output: n/a
        """

        #####Declerations#####

        #####Computations#####
        #Checks the submitted variable is an integer
        try:
            int(ndim)

        #If it isn't the correct type prints appropriat error for the kind of varibale and quits
        except:
            if sel == True:
                print('Number of rows must be an intger')
            elif sel == False:
                print('Number of columns must be an intger')

            quit()


        #Checks the variabe is a positive integer
        if ndim > 0:
            pass

        #If it isn't a positive int prints appropriat error for the kind of varibale and quits
        else:
            if sel == True:
                print('Number of rows must be a positive intger')
            elif sel == False:
                print('Number of columns must be a positive intger')

            quit()


class Conway_Abstract_Print(Conway_Input):
    "A Class with a function that only prints the alive squares"

    def print_grid_abstract(self,swi):
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



    def string_creation(self,aliveness,daswi):
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


#class Life_and_Death_rules(cb):
    "A Class that allows users to use custom life and death rules for the neighbour states"

#    def __init__():

#    def conway_life_death_comp(self, sum, index)
