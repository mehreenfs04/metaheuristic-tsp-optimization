import numpy as np
import random

class AntColonyOptimizer:
    def __init__(self, dist_matrix, n_ants=20, n_iterations=100, alpha=1.0, beta=2.0, rho=0.1, Q=100):
        """
        Args:
            dist_matrix: 2D array of distances between cities [cite: 26, 95]
            n_ants: Number of ants in each iteration [cite: 104]
            n_iterations: Max number of iterations [cite: 107]
            alpha: Pheromone importance [cite: 105]
            beta: Heuristic importance (distance inverse) [cite: 105]
            rho: Pheromone evaporation rate [cite: 106]
            Q: Pheromone deposit factor [cite: 101]
        """
        self.dist_matrix = dist_matrix
        self.n_cities = len(dist_matrix)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        
        # Initialize pheromones to a small constant value [cite: 96]
        self.pheromone = np.ones((self.n_cities, self.n_cities)) / self.n_cities
        # Heuristic information: 1/distance (avoid division by zero) [cite: 97]
        self.eta = 1.0 / (dist_matrix + np.eye(self.n_cities) * 1e-9)

    def run(self):
        best_tour = None
        best_dist = float('inf')

        for iteration in range(self.n_iterations):
            all_tours = []
            all_distances = []

            for ant in range(self.n_ants):
                tour = self._construct_path()
                dist = self._calculate_total_distance(tour)
                all_tours.append(tour)
                all_distances.append(dist)

                if dist < best_dist:
                    best_dist = dist
                    best_tour = tour

            self._update_pheromones(all_tours, all_distances)
            
            # Optional: Print progress for monitoring convergence [cite: 163]
            if (iteration + 1) % 10 == 0:
                print(f"Iteration {iteration+1}: Best distance = {best_dist:.2f}")

        return best_tour, best_dist

    def _construct_path(self):
        """Builds a path for one ant using the probabilistic transition rule [cite: 98]"""
        path = [random.randint(0, self.n_cities - 1)]
        visited = set(path)

        while len(visited) < self.n_cities:
            i = path[-1]
            # Calculate probabilities for next cities
            probabilities = []
            for j in range(self.n_cities):
                if j not in visited:
                    # Prob = (pheromone^alpha) * (heuristic^beta) [cite: 98]
                    tau = self.pheromone[i][j] ** self.alpha
                    eta = self.eta[i][j] ** self.beta
                    probabilities.append(tau * eta)
                else:
                    probabilities.append(0)

            # Normalize probabilities
            prob_sum = sum(probabilities)
            probabilities = [p / prob_sum for p in probabilities]

            # Choose next city based on roulette wheel selection [cite: 98]
            next_city = np.random.choice(range(self.n_cities), p=probabilities)
            path.append(next_city)
            visited.add(next_city)

        # Return to depot to complete the cycle [cite: 32]
        path.append(path[0])
        return path

    def _calculate_total_distance(self, tour):
        """Calculates total tour distance [cite: 33]"""
        distance = 0
        for i in range(len(tour) - 1):
            distance += self.dist_matrix[tour[i]][tour[i+1]]
        return distance

    def _update_pheromones(self, all_tours, all_distances):
        """Pheromone evaporation and reinforcement [cite: 99, 100, 101]"""
        # Evaporation: Pheromone = (1 - rho) * Pheromone [cite: 100]
        self.pheromone *= (1 - self.rho)

        # Reinforcement based on tour quality [cite: 101]
        for tour, dist in zip(all_tours, all_distances):
            deposit = self.Q / dist
            for i in range(len(tour) - 1):
                self.pheromone[tour[i]][tour[i+1]] += deposit
                self.pheromone[tour[i+1]][tour[i]] += deposit