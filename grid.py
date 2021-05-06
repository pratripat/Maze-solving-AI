from cell import Cell
from functions import *
import random

class Grid:
    def __init__(self, rows, cols, res):
        self.rows = rows
        self.cols = cols
        self.res = res
        self.cells = [Cell(i, j, self.res) for i in range(self.rows) for j in range(self.cols)]

        self.current = self.cells[0]
        self.current.visited = True
        self.stack = [self.current]

    def generate(self):
        #Generate maze
        while len(self.stack) > 0:
            self.update()

    def render(self, surface):
        #Renders all the cells in the maze
        for cell in self.cells:
            cell.render(surface)

    def update(self):
        #Get neighbors of the current cell
        neighbors = self.current.get_neighbors(self)

        #If there are no neighbors
        if len(neighbors) == 0:
            #If maze is generated already, stop
            if len(self.stack) == 0:
                return

            #Move to the previous current cell
            self.current = self.stack.pop()
            self.current.visited = True
            return

        #Choose one neighbor randomly
        random_neighbor = random.choice(neighbors)

        #Remove the walls between the neighbor and the current cell
        remove_wall(self.current, random_neighbor)

        #Make the neighbor the current cell
        self.current = random_neighbor
        self.current.visited = True

        #Add the neighbor to the stack
        self.stack.append(self.current)

    def get_cell(self, index):
        try:
            #Return None if the index is negative
            if index < 0:
                return None

            #Return the cell according to the index
            return self.cells[index]
        except:
            #If error occurs, return None
            return None
