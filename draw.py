# I/we declare that this file represents our own work, and that we
# have not seen any work on this assignment done by others, and that
# we have not shown our work to any others.

# Student name(s): Soumitra Koustubh Manavi, Jash Prakash Rana
# Student ID(s): 22220805, 22222806

# Do not change the formatting above. For multiple names/IDs, use
# commas to separate.


import math

def distance(x0, y0, x1, y1):
    # Euclidean distance between (x0, y0) and (x1, y1).
    # Don't change this.
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

def render(canvas):
    # This function takes in a canvas which has already been drawn on,
    # and prints it. Don't change this.
    for row in canvas:
        print(' '.join(row))

def draw(shapes, width, height):
    '''Draw a simple picture on a grid.

    A picture is specified as a list of shapes. Each shape is either a
    `disc` or a `rect`.

    `draw` creates the grid as a list of lists and draws the shapes.

    A second function, `render`, takes care of some details of
    printing correctly.

    The coordinate system starts at the top-left of the image.

    Here we draw a rectangle, using the 'colour' #,
    with top-left (0, 0), with width 2 and height 3,
    in a grid of width 10 and height 5
    >>> render(draw([['rect', '#', 0, 0, 2, 3]], 10, 5))
    # # . . . . . . . .
    # # . . . . . . . .
    # # . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .

    >>> render(draw([['disc', '#', 2, 2, 2]], 5, 5))
    . . . . .
    . # # # .
    . # # # .
    . # # # .
    . . . . .

    If a shape goes beyond the grid, we just draw the part that
    is inside the grid:
    >>> render(draw([['rect', '#', 3, 3, 9, 9]], 5, 5))
    . . . . .
    . . . . .
    . . . . .
    . . . # #
    . . . # #

    If one shape overlaps another, the later overwrites the earlier:
    >>> render(draw([['disc', '#', 10, 10, 5], ['rect', '=', 5, 5, 3, 5]], 20, 20))
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . = = = . . . . . . . . . . . .
    . . . . . = = = # # # # # . . . . . . .
    . . . . . = = = # # # # # # . . . . . .
    . . . . . = = = # # # # # # # . . . . .
    . . . . . = = = # # # # # # # . . . . .
    . . . . . . # # # # # # # # # . . . . .
    . . . . . . # # # # # # # # # . . . . .
    . . . . . . # # # # # # # # # . . . . .
    . . . . . . . # # # # # # # . . . . . .
    . . . . . . . . # # # # # . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .

    '''

    canvas = [['.' for _ in range(width)] for _ in range(height)]
    shape_rect = 'rect'
    shape_disc = 'disc'

    for list_index in shapes:

        # checking if the list contains 'disc' string in list_index[1]
        if list_index[0] == shape_disc:
            #assigning variables with the values given for disc
            colour = list_index[1]
            x_point = list_index[2]
            y_point = list_index[3]
            radius = list_index[4]

            for x1 in range(width):
                for y1 in range(height):
                    #checking the Euclidean distance for disc
                    grid_formation = distance(x_point, y_point, x1, y1)
                    if grid_formation < radius:
                        # updates the 'colour' at the point we are at in the grid
                        canvas[y1][x1] = colour

        # checking if the list contains 'rect' string in list_index[1]
        elif list_index[0] == shape_rect:
            #assigning variables with the values given for rect
            colour = list_index[1]
            x_point = list_index[2]
            y_point = list_index[3]
            x_limit = list_index[4]
            y_limit = list_index[5]

            for x in range(x_point, x_limit + x_point):
                for y in range(y_point, y_limit + y_point):
                    if x < width and y < height:
                        # updates the 'colour' at the point we are at in the grid
                        canvas[y][x] = colour

        #just trials and errors
        #     #canvas = [[shapes[1], shapes[2], shapes[3], shapes[4], shapes[5]]]
        #     for i,j in range(canvas[[shapes[4]]]),range(canvas[[shapes[5]]]):
        #         str = shapes[1]
        #         canvas = [str]
        ## YOUR CODE HERE
    return canvas




def owl():
    '''

    This function is a test. No need to change anything.

    >>> owl()
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . # # # # # . . . . .
    . . . . . . . . . . . . . . . . . . . # # # . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . # # # . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . # # # # # . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . = = . . . . . . = = . . . . . . . . . . . . . . .
    . . . . . = = . . . . . . = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . =       = =       = . . . . . . . . . . . . . . .
    . . . . . =       = =       = . . . . . . . . . . . . . . .
    . . . . . =       = =       = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    
    '''
    shapes = [
        ['disc', '#', 22, 8, 5],
        ['disc', '.', 24, 8, 4],
        ['rect', '=', 5, 18, 10, 12],
        ['rect', ' ', 6, 22, 3, 3],
        ['rect', ' ', 11, 22, 3, 3],
        ['rect', '.', 7, 18, 6, 2],
        ]
        
    render(draw(shapes, 30, 30))


def my_drawing():

    # Draw a picture of whatever you like.

    # No doctests needed for this function.

    # For this function, run it using $ python draw.py

    # Set width, height as you like.
    height, width = 30, 30

    shapes = [
        ## YOUR CODE HERE
        ['rect', '+', 1, 3, 27, 13],
        ['rect', ' ', 2, 4, 25, 3],
        ['rect', ' ', 2, 8, 25, 3],
        ['rect', ' ', 2, 12, 25, 3],
        ['disc', '0', 14, 9, 2.5],
        ['disc', '*', 14, 9, 1],
        ['rect', '╫', 0, 2, 2, 30],
        ['rect', '▲', 0, 1, 2, 2]
    ]
    render(draw(shapes, height, width))


if __name__ == '__main__':
    print('\n')
    print ('Behold the Flag of India!')
    print('\n')
    my_drawing()
