#
# COMP 1701 Fall 2024
# 
# Assignment 4 Game of Life
# 
# A. Fedoruk


from matplotlib import pyplot as plt


BIRTH_NEIGHBORS     = 3 # From GoL rules, with three neighbours, come alive!
SURVIVAL_NEIGHBORS  = 2 # With 2 neighbours, stay alive (or three)
N_STEPS             = 100 # Number of steps to run each game
BORDER              = '\u2592'
LIVE_CELL           = '\u2588'
UNALIVE_CELL        = ' '
FRAME_RATE          = 0.2


def view_grid( grid: list, frame_delay: float, step_number: int) -> None:
    """
    Shows an image of the current state of the grid
    parameters:
        grid - list-of-lists representing the current grid. Inner lists use 0s to represent dead cells, and 1s to represent live ones
        frame_delay - the program will pause for this many seconds after displaying the image. 0.1s gives a pretty good animation effect
        step_number - the step number of the supplied grid (will be displayed above the image)
    """

    # check that the grid supplied is not empty
    if len( grid) == 0:
        raise Exception( "grid is empty")

    # check that all rows contain the same number of cells
    row_lengths = set( [len(row) for row in grid])
    if len( row_lengths) != 1:
        raise Exception( f"not all grid rows are the same length. Found lengths: {row_lengths}")

    # check that all rows contain only 0s and 1s
    if not all( [set(row) <= {0, 1} for row in grid]):
        raise Exception( "only 0 and 1 are allowed in grid")

    # plot the grid
    plt.cla()
    plt.imshow( grid)
    plt.title( f'step {step_number}')
    plt.pause( frame_delay)


def load_board( filename: str) -> list:
    """ Load the starting configuration in filename (relative path) into a 2d binary list
    The file contains a border which will be loaded as 0s. So the active grid is 
    from 1 to n-1 in size. 
    """

    grid = []
    f = open( filename, 'r', encoding='UTF-8')

    for l in f:
        row = []
        line = l.strip() # remove the newline and any trailing spaces
        for character in line:
            if character == LIVE_CELL: # live cell
                row.append(1)
            else: # set blank cells and border cells to unalive
                row.append(0)
        grid.append( row)
    f.close()

    return grid


def save_grid( filename: str, grid: list) -> None:
    """ Saves the given board state to the relative path in filename"""

    f = open( filename, 'w', encoding='UTF-8')
    
    f.write( BORDER * ( len( grid[0])) + '\n') # write top border
    for row in grid[1:len( grid)-1]:
        f.write( BORDER)
        for r in row[1:len( row)-1]:
            if row == 1:
                f.write( LIVE_CELL)
            else:
                f.write( UNALIVE_CELL)
        f.write( BORDER + '\n')
    f.write( BORDER * ( len( grid[0])) + '\n') # write bottom border 
    f.close()


def get_empty_grid( rows:int, cols:int) -> list:
    """ Create an empty grid (2d list of all zeros) of the given size.
    """

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        grid.append( row)

    return grid


def count_neighbors( grid:list, row:int, col:int)->int:
    """ Count the number of live celled from the 8 neighbors of cell grid[row][col]. 
    """

    count = 0
    for r in range( row - 1, row + 2):
        for c in range( col - 1, col + 2):
            if not ( row == r and col == c): # don't count myself! 
                count += grid[r][c]
    # print(r,c,count)

    return count


def get_new_state( grid: list, r: int, c: int) -> int:
    """ Get the new state of cell grid[r][c] per the rules of the GoL
    """

    neighbors = count_neighbors( grid, r, c)
    
    if neighbors == BIRTH_NEIGHBORS:
        new_state = 1
    elif neighbors == SURVIVAL_NEIGHBORS:
        new_state = grid[r][c]
    else:
        new_state = 0
    
    return new_state


def print_grid( grid:list) -> None:
    """ For debugging. 
    """

    for r in grid:
        for c in r: 
            print(c, end='')
        print()



def main( input_filename: str, output_filename: str, display: bool) -> None:
    """
    main function
    parameters:
        input_filename: file to read the starting configuration from
        output_filename: file to write the ending configuration (after 100 steps) to
        display: if True, the program should display the grid steps (using the provided view_grid function)
                 if False, the program should not display the grid steps.
    """

    grid = load_board( input_filename)
    
    rows = len( grid)
    cols = len( grid[0])
    # print( "grid size = ", len( grid), len( grid[0]))
    # print_grid( grid)

    for step in range(N_STEPS):

        new_grid = get_empty_grid( rows, cols)
        # Use 1 to rows/cols -1 to skip the borders. 
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                new_grid[r][c] = get_new_state( grid, r, c)
        
        grid = new_grid

        if display:
            view_grid( grid, FRAME_RATE, step)
    
    save_grid( output_filename, grid)


main( './data/input/sheldon.txt', './data/output/expected_output_a.txt', True)

