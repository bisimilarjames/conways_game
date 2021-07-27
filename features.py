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

class Conway_Alternative_Grids(Conway_Abstract_Print):
    "A class that allows users to have alternative grid rules"

    def periodic_grid_update(self):
        """
        Updates the grid for each iteration of the run. This has been modified with the gird with periodic boundary conditions.

        data input: The int variables for the number of rows and columns, and the randomised grid storage array
        data output: The grid storage list with updated states for all the elements
        """
        #####Declerations#####
        ####Data Structures####
        #Makes an immutable copy of the current state of the grid
        reference = tuple(self.grid)
        ####Variables####
        #Variable for holding the number of neighbours of each grid
        sum = 0

        #####Computations#####
        #Loops through each element in the grid
        for i in range(len(self.grid)):
            # CORNERS
            #Checks if the current element is one of the corners
            #Top left corner
            #Grid takes from the three corners around it
            #The corner opposite it
            #The two grids directly at the bottom of the grid
            #The two elements direstly on the opposite side of the grid
            if (i == self.corner[0]):
                sum = (reference[self.row * self.col - 1] + reference[(self.row - 1) * self.col] + reference[(self.row - 1) * self.col + 1] +
                reference[self.col - 1] + reference[i + 1] +
                reference[2 * self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Top Right corner
            elif(i == self.corner[1]):
                sum = (reference[self.row * self.col - 2] + reference[self.row * self.col - 1] + reference[(self.row - 1) * self.col] +
                reference[i - 1] + reference[0] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + 1])


            #Bottom left corner
            elif(i == self.corner[2]):
                sum = (reference[i - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[self.row * self.col - 1] + reference[i + 1] +
                reference[self.col - 1] + reference[0] + reference[1])

            #Bottom right corner
            elif(i == self.corner[3]):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] + reference[i - 2 * self.col + 1] +
                reference[i - 1] + reference[i - self.col + 1] +
                reference[self.col - 2] + reference[self.col - 1] + reference[0])

            #EDGE
            #Checks if the current element is an edge element
            #Top Edge
            #Grid takes from the five grids arount it
            #And the three grids on the direct opposite side
            elif(i in self.top_edge):
                sum = (reference[(self.row - 1) * self.col + i - 1] + reference[(self.row - 1) * self.col + i] + reference[(self.row - 1) * self.col + i + 1] +
                reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Left Edge
            elif(i in self.left_edge):
                sum = (reference[i - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[i + self.col - 1] + reference[i + 1] +
                reference[i + self.col] + reference[i + self.col] + reference[i + self.col + 1])

            #Right Edge
            elif(i in self.right_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] + reference[i - 2 * self.col + 1] +
                reference[i - 1] + reference[i - self.col + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + 1])

            #Bottom Edge
            elif(i in self.bottom_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] + reference[i + 1 - self.col] +
                reference[i - 1] + reference[i + 1] +
                reference[i - 1 - (self.row - 1) * self.col] + reference[i - (self.row - 1) * self.col] + reference[1 + i - (self.row - 1) * self.col])

            #Core positions
            #Each core position has eight neighbours
            else:
                sum = (reference[i - self.col - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Checks the sum of the elements neighbours and updates the state
            self.conway_life_death_comp(sum, i)

            ####Garbage####
            #Resets the neighbours sum
            sum = 0
    def wrap_round_update(self):
        """
        Updates the grid for each iteration of the run. This has been modified with the grid with wrap round boundary conditions.

        data input: The int variables for the number of rows and columns, and the randomised grid storage array
        data output: The grid storage list with updated states for all the elements
        """
        #####Declerations#####
        ####Variables####
        #Needed to to store the position of i in the edge tuple
        edge_pos = 0
        ####Data Structures####
        #Makes an immutable copy of the current state of the grid
        reference = tuple(self.grid)
        ####Variables####
        #Variable for holding the number of neighbours of each grid
        sum = 0

        #####Computations#####
        #Loops through each element in the grid
        for i in range(len(self.grid)):
            # CORNERS
            #Checks if the current element is one of the corners
            #Top left corner
            #Grid takes from the three corners around it
            #The corner opposite it
            #And the two grids above the corner oppoisite
            #The the two grids left of the corner opposite
            if (i == self.corner[0]):
                sum = (reference[self.row * self.col - 1] + reference[self.row * self.col - 2] + reference[self.row * self.col - 3] +
                reference[(self.row - 1) * self.col - 1] + reference[i + 1] +
                reference[(self.row - 2)* self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Top Right corner
            elif(i == self.corner[1]):
                sum = (reference[(self.row - 1) * self.col + 2] + reference[(self.row - 1) * self.col + 1] + reference[(self.row - 1) * self.col] +
                reference[i - 1] + reference[(self.row - 2) * self.col] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[(self.row - 3) * self.col])


            #Bottom left corner
            elif(i == self.corner[2]):
                sum = (reference[3 * self.col - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[2 * self.col - 1] + reference[i + 1] +
                reference[self.col - 1] + reference[self.col - 2] + reference[self.col - 3])

            #Bottom right corner
            elif(i == self.corner[3]):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] + reference[2 * self.col] +
                reference[i - 1] + reference[self.col] +
                reference[2] + reference[1] + reference[0])

            #EDGE
            #Checks if the current element is an edge element
            #Top Edge
            #The five grids around it
            #The three girds on the bottom row that come from the oppoiste side of the edge
            #e.g. if i = 1 then the centre of the opposite is rc - i - 1
            elif(i in self.top_edge):
                sum = (reference[self.row * self.col - i] + reference[self.row * self.col - (i + 1)] + reference[self.row * self.col - (i + 2)] +
                reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Left Edge
            elif(i in self.left_edge):
                sum = (reference[i - self.col] + reference[i - self.col + 1] +
                reference[i + 1] +
                reference[i + self.col] + reference[i + self.col + 1])

                edge_pos = self.left_edge.index(i)
                #For figure out the indexes required of the opposite edge.
                #If it is the first index in the edge array
                if edge_pos == 0:
                    #Take the bottom right corner of the grid and the two grids above it
                    sum += (reference[self.row * self.col - 1] + reference[self.right_edge[-1]] + reference[self.right_edge[-2]])
                #If it is the last index in the edge array
                elif edge_pos == (len(self.left_edge) - 1):
                    #Take the top right corner of the grid and the two grids below it it
                    sum += (reference[self.col - 1] + reference[self.right_edge[0]] + reference[self.right_edge[1]])
                # All other indexs in the edge array
                else:
                    #Reverse index in the right edge storage tuple
                    sum += (reference[self.right_edge[-1 * (edge_pos + 2)]] + reference[self.right_edge[-1 * (edge_pos + 1)]] + reference[self.right_edge[-edge_pos]])

            #Right Edge
            elif(i in self.right_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] +
                reference[i - 1] +
                reference[i + self.col - 1] + reference[i + self.col])

                edge_pos = self.right_edge.index(i)

                if edge_pos == 0:
                    sum += (reference[(self.row - 1) * self.col] + reference[self.left_edge[-1]] + reference[self.left_edge[-2]])
                elif edge_pos == (len(self.right_edge) - 1):
                    sum += (reference[0] + reference[self.left_edge[0]] + reference[self.left_edge[1]])
                else:
                    sum += (reference[self.left_edge[-1 * (edge_pos + 2)]] + reference[self.left_edge[-1 * (edge_pos + 1)]] + reference[self.left_edge[-edge_pos]])

            #Bottom Edge
            elif(i in self.bottom_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] + reference[i + 1 - self.col] +
                reference[i - 1] + reference[i + 1] +
                reference[self.row * self.col - (i + 2)] + reference[self.row * self.col - (i + 1)] + reference[self.row * self.col - i])

            #Core positions
            #Each core position has eight neighbours
            else:
                sum = (reference[i - self.col - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Checks the sum of the elements neighbours and updates the state
            self.conway_life_death_comp(sum, i)

            ####Garbage####
            #Resets the neighbours sum
            sum = 0

    def cylinder_update(self):
        """
        Updates the grid for each iteration of the run. This has been modified with the gird being wrapped around into a cylinder

        data input: The int variables for the number of rows and columns, and the randomised grid storage array
        data output: The grid storage list with updated states for all the elements
        """
        #####Declerations#####
        ####Data Structures####
        #Makes an immutable copy of the current state of the grid
        reference = tuple(self.grid)
        ####Variables####
        #Variable for holding the number of neighbours of each grid
        sum = 0

        #####Computations#####
        #Loops through each element in the grid
        for i in range(len(self.grid)):
            # CORNERS
            #Checks if the current element is one of the corners
            #Top left corner
            #takes the three grids around it
            #And two on the opposite x coordinate side
            if (i == self.corner[0]):
                #Sums the state three grid neighbours of the top left corner element
                sum = (reference[i + 1] +
                reference[i + self.col] + reference[i + self.col + 1] +
                #cylinder rules
                reference[i + self.col - 1] + reference[i + 2 * self.col - 1])

            #Top Right corner
            elif(i == self.corner[1]):
                sum = (reference[i - 1] +
                reference[i + self.col - 1] + reference[i + self.col] +
                #cylinder rules
                reference[0] + reference[i + 1])

            #Bottom left corner
            elif(i == self.corner[2]):
                sum = (reference[i - self.col] + reference[i - self.col + 1] +
                reference[i + 1] +
                #cylinder rules
                reference[i - 1] + reference[i + self.col - 1])

            #Bottom right corner
            elif(i == self.corner[3]):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] +
                reference[i - 1] +
                #cylinder rules
                reference[i - self.col + 1] + reference[i - 2 * self.col + 1])

            #EDGE
            #Checks if the current element is an edge element
            #Top Edge
            #Takes the five grids around it
            elif(i in self.top_edge):
                sum = (reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Left Edge
            #Takes the five grids around it
            #And the three grids on the opposite x side
            elif(i in self.left_edge):
                sum = (reference[i - self.col] + reference[i - self.col + 1] +
                reference[i + 1] +
                reference[i + self.col] + reference[i + self.col + 1] +
                #cylinder rules
                reference[i - 1] + reference[i + self.col - 1] + reference[i + self.col])

            #Right Edge
            elif(i in self.right_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] +
                reference[i - 1] +
                reference[i + self.col - 1] + reference[i + self.col] +
                #cylinder rules
                reference[i - 2 * self.col + 1] + reference[i - self.col + 1] + reference[i + 1])

            #Bottom Edge
            elif(i in self.bottom_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] + reference[i + 1 - self.col] +
                reference[i - 1] + reference[i + 1])

            #Core positions
            #Each core position has eight neighbours
            else:
                sum = (reference[i - self.col - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Checks the sum of the elements neighbours and updates the state
            self.conway_life_death_comp(sum, i)

            ####Garbage####
            #Resets the neighbours sum
            sum = 0
