import random
import math

def tour_length(tour, dist_matrix):
    """Calculates total tour distance including return to start[cite: 129]."""
    total = 0.0
    n = len(tour)
    for i in range(n - 1):
        total += dist_matrix[tour[i]][tour[i + 1]]
    total += dist_matrix[tour[-1]][tour[0]]
    return total

def generate_neighbor(tour):
    """2-opt swap: Reverses a random segment of the tour."""
    new_tour = tour[:]
    i, j = sorted(random.sample(range(len(tour)), 2))
    new_tour[i:j] = reversed(new_tour[i:j])
    return new_tour

def acceptance_probability(delta, temperature):
    """Metropolis acceptance rule."""
    if delta < 0:
        return 1.0
    return math.exp(-delta / temperature)

def simulated_annealing(dist_matrix, initial_temp=1000, cooling_rate=0.995, n_iterations=10000):
    """Main SA Algorithm for TSP."""
    n = len(dist_matrix)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_length = tour_length(current_tour, dist_matrix)

    best_tour = current_tour[:]
    best_length = current_length
    temp = initial_temp

    for _ in range(n_iterations):
        neighbor = generate_neighbor(current_tour)
        neighbor_length = tour_length(neighbor, dist_matrix)
        delta = neighbor_length - current_length

        if random.random() < acceptance_probability(delta, temp):
            current_tour = neighbor
            current_length = neighbor_length

            if current_length < best_length:
                best_tour = current_tour[:]
                best_length = current_length

        temp *= cooling_rate 

    return best_tour, best_length