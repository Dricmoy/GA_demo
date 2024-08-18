import random
import pygame 

class Path:
    def __init__(self, length, start, end, maze):
        self.moves = [random.randint(0, 3) for _ in range(length)]
        self.start = start
        self.end = end
        self.maze = maze
        self.fitness_score = None
    
    def calculate_fitness(self):
        x, y = self.start
        for move in self.moves:
            if move == 0: y -= 1
            elif move == 1: y += 1
            elif move == 2: x -= 1
            elif move == 3: x += 1
            
            # Check if out of bounds or hit a wall
            if x < 0 or x >= self.maze.width or y < 0 or y >= self.maze.height or self.maze.is_wall(x, y):
                break
        
        # Calculate fitness based on distance to the end point
        distance = abs(self.end[0] - x) + abs(self.end[1] - y)
        self.fitness_score = 1 / (1 + distance)
        return self.fitness_score
    
    def mutate(self, mutation_rate=0.01):
        for i in range(len(self.moves)):
            if random.random() < mutation_rate:
                self.moves[i] = random.randint(0, 3)
    
    def crossover(self, other):
        crossover_point = random.randint(0, len(self.moves) - 1)
        child_moves = self.moves[:crossover_point] + other.moves[crossover_point:]
        return Path(len(child_moves), self.start, self.end, self.maze)
    
    def draw(self, window, color=(0, 255, 0)):
        x, y = self.start
        for move in self.moves:
            if move == 0: y -= 1
            elif move == 1: y += 1
            elif move == 2: x -= 1
            elif move == 3: x += 1
            
            # Check if out of bounds or hit a wall
            if x < 0 or x >= self.maze.width or y < 0 or y >= self.maze.height or self.maze.is_wall(x, y):
                break
            
            pygame.draw.rect(window, color, (x * self.maze.cell_size, y * self.maze.cell_size, self.maze.cell_size, self.maze.cell_size))
