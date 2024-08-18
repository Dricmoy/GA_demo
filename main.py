import pygame  # Pygame is used for visualization
import random  # Random is used for mutations and crossover
from maze import Maze  # Import the Maze class
from path import Path  # Import the Path class
from geneticalgorithm import GeneticAlgorithm  # Import the GeneticAlgorithm class
from visualizer import Visualizer  # Import the Visualizer class


CELL_SIZE = 90  # Size of each cell in the maze
WIDTH = 8 * CELL_SIZE  # Width of the window (based on maze size)
HEIGHT = 7 * CELL_SIZE  # Height of the window (based on maze size)

# Maze grid
maze_grid = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Start and end points
start_point = (0, 0)
end_point = (7, 6)

# Create maze, genetic algorithm, and visualizer
maze = Maze(maze_grid, CELL_SIZE)
algorithm = GeneticAlgorithm(population_size=100, path_length=20, start=start_point, end=end_point, maze=maze)
visualizer = Visualizer(maze, algorithm, WIDTH, HEIGHT)

# Run the visualizer
visualizer.run()
