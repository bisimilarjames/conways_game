import random

class Conway_Base:
    """Base conway game of life class"""

    def __init__(self,dim):
        """Initialises the conway grid in a square"""
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
        """Creates the array that stores states of the of the game"""

        self.grid = [0 for i in range(0,self.row * self.col)]

    def edge_and_corner_calc(self):
            """Does the pre-calculations of all the corners and edges positions in the grid"""

            #Creates an array with the corner positions of the grid in the array
            self.corner = [0, self.col-1, (self.row - 1) * self.col, self.row * self. col - 1]

            #Edge arrays
            #Top edge
            self.top_edge = [i for i in range(1, self.col-1)]
            #Left edge
            self.left_edge = [i for i in range(self.col, (self.row - 2)* self.col + 1, self.col)]
            #Right edge
            self.right_edge = [i for i in range(2 * self.col - 1, (self.row - 1) * self.col, self.col)]
            #Bottom edge
            self.bottom_edge = [i for i in range((self.row - 1) * self.col + 1, self.row * self. col - 1)]

    def create_grid(self):
        """creates an initial grid layout using coin flip cunction"""

        for i in range(len(self.grid)):
            x = random.random()
            if x < 0.5:
                self.grid[i] = 0
            else:
                self.grid[i] = 1

    def print_grid(self):
        """Prints the conway grid in the terminal"""
        for i in range(self.row):
            print(self.grid[0 + self.col*i:self.col * (1 + i)] )
        print('\n')
    def grid_update(self):
        """Updates the grid for each iteration of the run"""

        reference = tuple(self.grid)
        sum = 0


        for i in range(len(self.grid)):
            # CORNERS
            #Top left corner
            if (i == self.corner[0]):
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
            else:
                sum = (reference[i - self.col - 1] + reference[i - self.col] + reference[i - self.col + 1] +
                reference[i - 1] + reference[i + 1] +
                reference[i + self.col - 1] + reference[i + self.col] + reference[i + self.col + 1])

            self.conway_life_death_comp(sum, i)

            sum = 0

    def conway_life_death_comp(self, sum, index):
        """Does the comparison to see if the state is alive or dead in the next iteration"""

        if 2 <= sum <=3:
            self.grid[index] = 1
        else:
            self.grid[index] = 0

class Conway_Abstract_Print(Conway_Base):
    """A Class with a function that only prints the alive squares"""

    def print_grid_abstract(self):

        alive = []
        for i in range(self.row):
            alive = [index for index, value in enumerate(self.grid[0 + self.col*i:self.col * (1 + i)]) if value == 1]
            print(self.string_creation(alive))

        print('\n')

    def string_creation(self,aliveness):
        printstore = ['X' if x in aliveness else '\t' for x in range(self.col)]
        printout = ''

        return(printout.join(printstore))
