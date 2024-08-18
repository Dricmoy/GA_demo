import random  # Random is used for mutations and crossover
from path import Path  # Import the Path class

class GeneticAlgorithm:
    def __init__(self, population_size, path_length, start, end, maze):
        self.population = [Path(path_length, start, end, maze) for _ in range(population_size)]
    
    def evolve(self):
        # Calculate fitness for each path
        fitnesses = [individual.calculate_fitness() for individual in self.population]
        
        # Create a new population
        new_population = []
        for _ in range(len(self.population)):
            parent1 = self.selection(fitnesses)
            parent2 = self.selection(fitnesses)
            child = parent1.crossover(parent2)
            child.mutate()
            new_population.append(child)
        
        self.population = new_population
    
    def selection(self, fitnesses):
        index = random.choices(range(len(self.population)), weights=fitnesses, k=1)[0]
        return self.population[index]
    
    def get_best_individual(self):
        return max(self.population, key=lambda individual: individual.calculate_fitness())
