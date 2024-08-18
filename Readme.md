# Genetic Pathways: Maze Evolution Simulator

![Demo Video](https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg)
[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID/hqdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## Overview

Welcome to **Genetic Pathways: Maze Evolution Simulator**! This project leverages genetic algorithms to find optimal paths through a maze. Watch as the algorithm evolves a population of paths, improving them over generations to navigate the maze from start to finish. Real-time visualization of the maze and the evolving paths is provided using Pygame.

## Features

- Real-time maze and path visualization.
- Genetic algorithm to evolve and optimize paths.
- Display of fitness scores, mutation rates, and generation information.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Dricmoy/GA_demo.git
    cd GA_demo
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that you have Pygame installed. If not, install it using:

    ```bash
    pip install pygame
    ```

2. Run the main program:

    ```bash
    python main.py
    ```

3. The visualizer will open, showing the maze and the evolving paths. The program will continue to run, evolving the paths and displaying real-time statistics until you close the window.

## Files

- **`main.py`**: The entry point for the application, initializes and runs the visualizer.
- **`maze.py`**: Defines the Maze class for creating and handling the maze grid.
- **`path.py`**: Defines the Path class representing a path through the maze.
- **`genetic_algorithm.py`**: Implements the GeneticAlgorithm class for evolving paths.
- **`visualizer.py`**: Contains the Visualizer class for displaying the maze and the paths.

## Contributing

Feel free to contribute to this project by opening issues, submitting pull requests, or suggesting improvements.

## Credits

- **Dricmoy Bhattacharjee**: Developer and maintainer of this project.
- **Pygame**: Used for visualization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

