import pygame, sys
from grid import Grid
from ai import AI

#Get the number of rows and cols from the user.
rows = cols = int(input('Enter the number of rows and cols: '))

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Maze Solver')

#Calculating res of each cell
res = screen.get_height()//rows

def main():
    #Initializing the maze.
    grid = Grid(rows, cols, res)
    grid.generate()

    #Initialize the ai
    ai = AI(grid.cells[0], grid.cells[(rows-1)*cols+(cols-1)], grid)

    while True:
        for event in pygame.event.get():
            #Quiting if asked to
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #Ai searches for path
        ai.search()

        #Renders maze and ai's path from start
        grid.render(screen)
        ai.render_path(screen)

        pygame.display.update()

main()
