import pygame

class Visualizer:
    def __init__(self, maze, algorithm, width, height):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Genetic Algorithm Maze Solver")
        self.maze = maze
        self.algorithm = algorithm
        self.running = True
    
    def draw(self):
        self.window.fill((255, 255, 255))
        self.maze.draw(self.window)
        best_path = self.algorithm.get_best_individual()
        best_path.draw(self.window)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.algorithm.evolve()
            self.draw()
            pygame.time.delay(100)
        
        pygame.quit()
