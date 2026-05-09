# Metaheuristic TSP Optimization

Implementation and comparative analysis of Ant Colony Optimization (ACO) and Simulated Annealing (SA) for solving the NP-Hard Traveling Salesperson Problem (TSP).

## Project Overview

This project models a logistics routing problem as a Traveling Salesperson Problem, where a route must visit each hospital exactly once and return to the starting depot while minimizing total travel distance.

Since TSP is NP-Hard, exact solutions become impractical for larger instances. This project compares two metaheuristic approaches:

- Ant Colony Optimization
- Simulated Annealing

## Technologies Used

- Python
- NumPy
- Matplotlib
- Algorithms
- Optimization
- Metaheuristics

## Features

- Synthetic TSP instance generation
- Euclidean distance matrix calculation
- Brute-force solver for small instances
- Ant Colony Optimization implementation
- Simulated Annealing implementation
- Runtime comparison
- Solution quality comparison
- Convergence visualization

## Project Structure

```bash
.
├── Datasets/
│   ├── tsp_10_test.txt
│   ├── tsp_20.txt
│   ├── tsp_50.txt
│   └── tsp_100.txt
├── main.py
├── Antcolonyoptimization.py
├── simulatedannealing.py
├── bruteforce_tsp.py
├── distancematrix.py
├── loadhospitals.py
├── datageneration.py
├── convergenceplot.py
└── TermProject.pdf
