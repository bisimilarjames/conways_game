from conway import Conway_Base as cb

class Conway_Input(cb):
    "A class whose initialisation allows for the generic arguments so a rectanglular grid can be constructed"

    def __init__(self, row, col):
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

        #Checks the inputs
        self.input_checker(row, True)
        self.input_checker(col, False)

        #Assigns the user input to the classes row and column variables
        super().__init__(row, col)

    def input_checker(self, ndim, sel):
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
        #The integer has to be greater that 3 for the corner and edge maths to work
        if ndim >= 3:
            pass

        #If it isn't a positive int prints appropriat error for the kind of varibale and quits
        else:
            if sel == True:
                print('Number of rows must be a positive intger, greater than or equal to 3.')
            elif sel == False:
                print('Number of columns must be a positive intger, greater than or equal to 3.')

            quit()

class Life_and_Death_rules(Conway_Input):
    "A Class that allows users to use custom life and death rules for the neighbour states"

    def __init__(self, *args):
        """
        Initialises class
        Passes row and columns to parent class
        Checks the birth and survival rules submitted

        data input: Tuples of birth and survival rules, and row and col (int) dimensions
        data output: Sets containing the birth and survival rules
        """
        #####Declerations#####
        rd = 0
        cd = 0

        #####Computations#####
        rd = args[0]
        cd = args[1]

        #Passes row and column dimensions to the conway input class
        super().__init__(rd, cd)

        if len(args) == 2:
            self.born_rules = (3)
            self.survive_rules = (2,3)
        elif len(args) == 4:
            #Checks the birth rules and sets them as a set
            self.born_rules = self.rule_checker(args[2], True)
            #Checks the survive rules and sets them as a set
            self.survive_rules = self.rule_checker(args[3], False)
        else:
            print('This program only accepts either 2 or 4 arguments')
            quit()


    def rule_checker(self, tup, sel):
        """
        Checks that the rule set content submitted are correct and return them as a set


        data input: A tuple
        data output: A tuple
        """
        #####Declerations#####
        ####Sets####
        #A square grid has a maximum of 8 neighbours so any comparison to the numbers of neighbours
        # has to be between 0 and 8
        comparison_set = {0,1,2,3,4,5,6,7,8}
        #Set holds the tuple submitted
        #Using a set removes any duplicate submissions from the user
        storage_set = set()
        #Holds the tuple that is used in the comparison operations
        test_set = set()


        #####Computations#####
        #If the tuple only has one element it defaults to whatever the type of the member is
        #The indvidual type is not iterable
        #If it is a tuple
        if type(tup) is tuple:
            #Loops through the members
            for item in tup:
                #If a member isn't an integer print the message for the correct rule set
                if not isinstance(item, int):
                    if sel == True:
                        print('Integers only in the born rules')
                    elif sel == False:
                        print('Integers only in the survive rules')
                    #Quits
                    quit()

        #If it is an indvidual thing submitted, the code only wants ints
        #If it isn't an int the code breaks
        elif type(tup) is not int:
            if sel == True:
                print('Integers only in the born rules')
            elif sel == False:
                print('Integers only in the survive rules')

            quit()

        #If it is an indvidual element
        if type(tup) is int:
            #It adds it to the empty set
            storage_set.add(tup)
        else:
            #Or it converts the tuple to set
            storage_set = set(tup)

        #If the user submits doesn't submit an empty rule set (which is allowed)
        if len(storage_set) != 0:
            #Make a test set of the submitted values and any missing in the comparison set
            test_set = storage_set.union(comparison_set)
            # If there are elements in the set that are not in the comparison set
            #Flags an error
            if len(test_set.difference(comparison_set)) != 0:
                if sel == True:
                    print('A grid can only have 0 to 8 neighbours. In the born rules.')
                elif sel == False:
                    print('A grid can only have 0 to 8 neighbours. In the survive rules.')

                quit()

        #Returns the set
        return tuple(storage_set)

    def conway_life_death_comp(self, sum, index):
        """
        An updated comparison to see if the state is alive or dead in the next iteration
        Using user generated rules

        data input: The current element index (int), the sum value for the current element (int <= 8), the grid state list
        and the birth and survive comparison sets (set)
        data output: The grid state list with the index updated for the next iteration
        """
        #####Declerations#####

        #####Computations#####
        # If the state is current alive
        if self.grid[index] == 1:
            #Is this sum equal to the user defined survivable number of neighbors
            #If it isn't set to dead
            if type(self.survive_rules) == tuple:
                if sum not in self.survive_rules:
                    self.grid[index] = 0
            # If the user only submits one value the type defaults to int which is not iterable
            else:
                if sum != self.survive_rules:
                    self.grid[index] = 0
        #If the surrent state is dead
        else:
            #If the sum is in the user defined birthing number of neighbours
            if type(self.born_rules) == tuple:
                if sum in self.born_rules:
                    #Sett to alive
                    self.grid[index] = 1
            # If the user only submits one value the type defaults to int which is not iterable
            else:
                if sum == self.born_rules:
                    #Sett to alive
                    self.grid[index] = 1
