def get_index(i, j, rows, cols):
    #Returns 1d index from 2d index
    if i < 0 or j < 0 or i > rows-1 or j > cols-1:
        return -1

    return i*cols+j

def remove_wall(cell1, cell2):
    #Removes wall between two cells
    if cell1.i - cell2.i == 1:
        cell1.walls[0] = False
        cell2.walls[2] = False
    if cell2.i - cell1.i == 1:
        cell1.walls[2] = False
        cell2.walls[0] = False
    if cell1.j - cell2.j == 1:
        cell1.walls[3] = False
        cell2.walls[1] = False
    if cell2.j - cell1.j == 1:
        cell1.walls[1] = False
        cell2.walls[3] = False
