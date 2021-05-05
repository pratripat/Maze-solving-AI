import pygame
from functions import *

class Cell:
    def __init__(self, i, j, res):
        self.i = i
        self.j = j
        self.res = res
        self.visited = False
        self.walls = [True, True, True, True]

    def render(self, surface):
        if self.visited:
            pygame.draw.rect(surface, (49,78,82), (self.j*self.res, self.i*self.res, self.res, self.res))

        self.render_walls(surface)

    def render_walls(self, surface):
        for i, wall in enumerate(self.walls):
            if not wall:
                continue

            if i == 0:
                pygame.draw.line(surface, (0,0,0), (self.j*self.res, self.i*self.res), ((self.j+1)*self.res, self.i*self.res))
            if i == 1:
                pygame.draw.line(surface, (0,0,0), ((self.j+1)*self.res, self.i*self.res), ((self.j+1)*self.res, (self.i+1)*self.res))
            if i == 2:
                pygame.draw.line(surface, (0,0,0), (self.j*self.res, (self.i+1)*self.res), ((self.j+1)*self.res, (self.i+1)*self.res))
            if i == 3:
                pygame.draw.line(surface, (0,0,0), (self.j*self.res, self.i*self.res), (self.j*self.res, (self.i+1)*self.res))

    def get_neighbors(self, grid):
        neighbors = []
        top = grid.get_cell(get_index(self.i-1, self.j, grid.rows, grid.cols))
        right = grid.get_cell(get_index(self.i, self.j+1, grid.rows, grid.cols))
        bottom = grid.get_cell(get_index(self.i+1, self.j, grid.rows, grid.cols))
        left = grid.get_cell(get_index(self.i, self.j-1, grid.rows, grid.cols))

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        return neighbors
