import pygame

class Maze:
    def __init__(self, grid, cell_size):
        self.grid = grid
        self.cell_size = cell_size
        self.width = len(grid[0])
        self.height = len(grid)
    
    def draw(self, window):
        for y in range(self.height):
            for x in range(self.width):
                color = (0, 0, 0) if self.grid[y][x] == 1 else (255, 255, 255)
                pygame.draw.rect(window, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def is_wall(self, x, y):
        return self.grid[y][x] == 1
