from itertools import permutations

def generate_tsp_permutations(dist_matrix):
    n = len(dist_matrix)
    cities_to_visit = list(range(1, n))
    min_dist = float("inf")
    best_tour = None
    
    import math
    total_perms = math.factorial(n-1)
    print(f"Checking {total_perms} permutations...")

    for count, p in enumerate(permutations(cities_to_visit)):
        current_tour = [0] + list(p) + [0]
        current_dist = 0
        for i in range(len(current_tour)-1):
            current_dist += dist_matrix[current_tour[i]][current_tour[i+1]]

        if current_dist < min_dist:
            min_dist = current_dist
            best_tour = current_tour
        
        if count % 100000 == 0 and count > 0:
            print(f"Progress: {count}/{total_perms} permutations searched...")
            
    return best_tour, min_dist