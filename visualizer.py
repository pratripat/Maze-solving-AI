import pygame, sys
from grid import Grid
from ai import AI

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Maze Solver')

rows = cols = 50
res = screen.get_height()//rows

def main():
    grid = Grid(rows, cols, res)
    grid.generate()

    ai = AI(grid.cells[0], grid.cells[(rows-1)*cols+(cols-1)], grid)

    clock = pygame.time.Clock()

    grid.render(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        ai.search()
        # grid.render(screen)
        ai.render_path(screen)

        pygame.display.update()

main()
