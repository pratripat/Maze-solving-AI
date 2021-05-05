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
        while len(self.stack) > 0:
            self.update()

    def render(self, surface):
        for cell in self.cells:
            cell.render(surface)

    def update(self):
        neighbors = self.current.get_neighbors(self)

        if len(neighbors) == 0:
            if len(self.stack) == 0:
                return

            self.current = self.stack.pop()
            self.current.visited = True
            return

        random_neighbor = random.choice(neighbors)

        remove_wall(self.current, random_neighbor)
        self.current = random_neighbor
        self.current.visited = True

        self.stack.append(self.current)

    def get_cell(self, index):
        try:
            if index < 0:
                return None

            return self.cells[index]
        except:
            return None
