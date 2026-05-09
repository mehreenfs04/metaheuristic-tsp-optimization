import time
import distancematrix
from loadhospitals import load_hospitals
from bruteforce_tsp import generate_tsp_permutations
from Antcolonyoptimization import AntColonyOptimizer
from simulatedannealing import simulated_annealing 

def run_experiment(filename):
    print(f"\n{'='*20}")
    print(f"RUNNING INSTANCE: {filename}")
    print(f"{'='*20}")

    cities = load_hospitals(filename)
    matrix = distancematrix.create_distance_matrix(cities)
    n = len(cities)
    
    # 1. BRUTE FORCE 
    if n <= 10:
        print("Calculating Optimal Solution (Brute Force)...")
        path_bf, dist_bf = generate_tsp_permutations(matrix)
        print(f"-> Optimal: {dist_bf:.2f}")
    else:
        dist_bf = None
        print(f"Skipping Brute Force (n={n} is too large for NP-Hard exact solving).")

    # 2. ANT COLONY OPTIMIZATION
    # Task 3: n_ants=20, n_iterations=100 
    aco = AntColonyOptimizer(matrix, n_ants=20, n_iterations=100)
    start_aco = time.perf_counter()
    path_aco, dist_aco = aco.run()
    end_aco = time.perf_counter()
    aco_runtime = end_aco - start_aco
    print(f"-> ACO Best: {dist_aco:.2f} | Runtime: {aco_runtime:.4f}s")

    # 3. SIMULATED ANNEALING
    # Task 4: Tuning iterations for larger N 
    sa_iters = 50000 if n >= 100 else 20000
    start_sa = time.perf_counter() #
    path_sa, dist_sa = simulated_annealing(matrix, n_iterations=sa_iters)
    end_sa = time.perf_counter()
    sa_runtime = end_sa - start_sa
    print(f"-> SA Best:  {dist_sa:.2f} | Runtime: {sa_runtime:.4f}s")

    return aco_runtime, sa_runtime

    # 4. RATIO CALCULATION 
    if dist_bf:
        print(f"ACO Approx Ratio: {dist_aco/dist_bf:.3f}")
        print(f"SA Approx Ratio:  {dist_sa/dist_bf:.3f}")

# Execute the full project suite
test_files = ["tsp_10_test.txt", "tsp_20.txt", "tsp_50.txt", "tsp_100.txt"]
for f in test_files:
    run_experiment(f)