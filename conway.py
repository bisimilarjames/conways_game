import random

class Conway_Base:
    "Base class for a Conway's game of life simulation"

    def __init__(self,dim):
        """
        Initialises the class
        Takes in length of a square grid
        Creates an array that will hold the state of each grid element
        Precalculates the array indicies that are corners and edges

        data input: a single int for the edge length of the grid
        data output: A list that stores the grids states
                     A series of tuples that stores the indicies of the grid elements that are on the corners and the edges
        """
        #####Declerations#####
        ####Variables####
        #Initialises the grid dimensions
        self.row = dim
        self.col = dim

        #####Computations#####
        #Creates grid storage array
        self.grid_setup()
        #Pre-calculates the edges and corner positions in the array
        self.edge_and_corner_calc()


    def grid_setup(self):
        """
        Creates the array that stores states of the of the game

        data input: The int variables for the number of rows and columns
        data output: The grid storage list with all the elements set to dead
        """
        #####Declerations#####

        #####Computations#####
        #The grid is represented as each row of grid elements aligned in one long row
        #[r_1,r_2,...,r_r]
        self.grid = [0 for i in range(0,self.row * self.col)]


    def edge_and_corner_calc(self):
        """
        Does the pre-calculations of all the corners and edges positions in the grid

        data input: Int values of the number of rows and columns
        data output: A Corner tuple of length 4, each element is a corner index
                     4 tuples that store the grid indicies for the edge elements
        """
        #####Declerations#####

        #####Computations#####
        #Creates an array with the corner positions of the grid in the array
        #Ordered top left, top right, bottom left, bottom right
        self.corner = (0, self.col-1, (self.row - 1) * self.col, self.row * self. col - 1)

        #Edge arrays
        #Top edge
        self.top_edge = tuple([i for i in range(1, self.col-1)])
        #Left edge
        self.left_edge = tuple([i for i in range(self.col, (self.row - 2)* self.col + 1, self.col)])
        #Right edge
        self.right_edge = tuple([i for i in range(2 * self.col - 1, (self.row - 1) * self.col, self.col)])
        #Bottom edge
        self.bottom_edge = tuple([i for i in range((self.row - 1) * self.col + 1, self.row * self. col - 1)])


    def create_grid(self):
        """
        creates an initial randomised grid layout

        data input: The int variables for the number of rows and columns, and the grid storage list filled with dead elements
        data output: The grid storage list with randomised alive and dead elements
        """
        #####Declerations#####

        #####Computations#####
        #Loops through each grid element. If the random number generator produces less than 0.5 it floors
        #Others the element is one
        self.grid = [0 if random.random() < 0.5 else 1 for x in range(self.row * self.col)]


    def print_grid(self):
        """
        Prints the conway grid in the terminal

        data input: The int variables for the number of rows and columns, and the randomised grid storage list
        data output: n/a
        """
        #####Declerations#####

        #####Computations#####
        #Loops through each row in the grid
        for i in range(self.row):
            #Prints out each row of the grid
            print(self.grid[0 + self.col*i : self.col * (1 + i)] )

        #New line to seperate the grids in the terminal
        print('\n')


    def grid_update(self):
        """
        Updates the grid for each iteration of the run

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
            #Each corner element has three neighbours
            #Top left corner
            if (i == self.corner[0]):
                #Sums the state three grid neighbours of the top left corner element
                sum = (reference[i + 1] +
                reference[i + self.col] + reference[i + self.col + 1])

            #Top Right corner
            elif(i == self.corner[1]):
                sum = (reference[i - 1] +
                reference[i + self.col - 1] + reference[i + self.col])

            #Bottom left corner
            elif(i == self.corner[2]):
                sum = (reference[i - self.col] + reference[i - self.col + 1] +
                reference[i + 1])

            #Bottom right corner
            elif(i == self.corner[3]):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] +
                reference[i - 1])

            #EDGE
            #Checks if the current element is an edge element
            #Each edge element has five neighbours
            #Top Edge
            elif(i in self.top_edge):
                sum = (reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            #Left Edge
            elif(i in self.left_edge):
                sum = (reference[i - self.col] + reference[i - self.col + 1] +
                reference[i + 1] +
                reference[i + self.col] + reference[i + self.col + 1])

            #Right Edge
            elif(i in self.right_edge):
                sum = (reference[i - (self.col + 1)] + reference[i - self.col] +
                reference[i - 1] +
                reference[i + self.col - 1] + reference[i + self.col])

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


    def conway_life_death_comp(self, sum, index):
        """
        Does the comparison to see if the state is alive or dead in the next iteration

        data input: The current element index (int), the sum value for the current element (int <= 8) and the grid state list
        data output: The grid state list with the index updated for the next iteration
        """
        #####Declerations#####

        #####Computations#####
        #If the element has 2 or 3 alive neighbours it remains alive in the next iteration
        if 2 <= sum <=3:
            self.grid[index] = 1
        #Any other number of neighbours the state dies in the next iteration
        else:
            self.grid[index] = 0
