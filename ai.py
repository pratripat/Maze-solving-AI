import random, pygame
from functions import *

class AI:
    def __init__(self, start, end, grid):
        self.previous = None
        self.current = start
        self.end = end
        self.grid = grid
        self.path = [start]
        self.visited = []
        self.searching = True

    def render_path(self, surface, render_visited=True):
        #Renders the path from start to the current position.
        for i in range(len(self.path)-1):
            pygame.draw.line(surface, (255,255,0), ((self.path[i].j+0.5)*self.grid.res, (self.path[i].i+0.5)*self.grid.res), ((self.path[i+1].j+0.5)*self.grid.res, (self.path[i+1].i+0.5)*self.grid.res))

        #If stopped searching or asked not to render further, return.
        if not render_visited or not self.searching:
            return

        #Renders the area that has been visited and does not lead to the solution.
        for cell in self.visited:
            pygame.draw.rect(surface, (0,0,0), (cell.j*self.grid.res, cell.i*self.grid.res, self.grid.res, self.grid.res))

    def get_neighbor(self, cell, index):
        #Returns the neighbor of the given cell, according to the index.
        top = self.grid.get_cell(get_index(cell.i-1, cell.j, self.grid.rows, self.grid.cols))
        right = self.grid.get_cell(get_index(cell.i, cell.j+1, self.grid.rows, self.grid.cols))
        bottom = self.grid.get_cell(get_index(cell.i+1, cell.j, self.grid.rows, self.grid.cols))
        left = self.grid.get_cell(get_index(cell.i, cell.j-1, self.grid.rows, self.grid.cols))

        neighbors = [top, right, bottom, left]

        return neighbors[index]

    def solve(self):
        #Solves the whole puzzle
        while self.searching:
            self.search()

    def search(self):
        #If solution is found, no need to search anymore
        if not self.searching:
            return

        #All the paths that it can take from the current position
        paths = [j for j, wall in enumerate(self.current.walls) if not wall]

        for i in range(len(paths)):
            path = paths[i]
            neighbor = self.get_neighbor(self.current, path)

            #If neighbor was not the previous current, or it is not in the visited list, then move to that position
            if neighbor != self.previous and neighbor not in self.visited:
                self.previous = self.current
                self.current = neighbor
                self.path.append(neighbor)

                #If the end is reached, then it does not need to search anymore
                if self.current == self.end:
                    self.searching = False

                return

        #If no path was found (it is stuck), go back and make sure to mark this as visited
        self.visited.append(self.current)
        self.current = self.previous
        self.previous = self.path[-3]
        self.path.pop()
