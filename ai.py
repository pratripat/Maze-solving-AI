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
        for i in range(len(self.path)-1):
            pygame.draw.line(surface, (255,255,0), ((self.path[i].j+0.5)*self.grid.res, (self.path[i].i+0.5)*self.grid.res), ((self.path[i+1].j+0.5)*self.grid.res, (self.path[i+1].i+0.5)*self.grid.res))

        if not render_visited:
            return

        for cell in self.visited:
            pygame.draw.rect(surface, (0,0,0), (cell.j*self.grid.res, cell.i*self.grid.res, self.grid.res, self.grid.res))

    def get_neighbor(self, cell, index):
        top = self.grid.get_cell(get_index(cell.i-1, cell.j, self.grid.rows, self.grid.cols))
        right = self.grid.get_cell(get_index(cell.i, cell.j+1, self.grid.rows, self.grid.cols))
        bottom = self.grid.get_cell(get_index(cell.i+1, cell.j, self.grid.rows, self.grid.cols))
        left = self.grid.get_cell(get_index(cell.i, cell.j-1, self.grid.rows, self.grid.cols))

        neighbors = [top, right, bottom, left]

        return neighbors[index]

    def solve(self):
        while self.searching:
            self.search()

    def search(self):
        if not self.searching:
            return

        i = 0
        paths = [j for j, wall in enumerate(self.current.walls) if not wall]

        while i < len(paths):
            path = paths[i]
            neighbor = self.get_neighbor(self.current, path)

            if neighbor != self.previous and neighbor not in self.visited:
                self.previous = self.current
                self.current = neighbor
                self.path.append(neighbor)

                if self.current == self.end:
                    self.searching = False

                return

            i += 1

        self.visited.append(self.current)
        self.current = self.previous
        self.previous = self.path[-3]
        self.path.pop()
