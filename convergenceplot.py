import matplotlib.pyplot as plt
n = [10, 20, 50, 100]

aco_runtime = [0.221, 0.523, 2.256, 8.165]
sa_runtime  = [0.062, 0.090, 0.171, 0.835]

aco_best = [3189.66, 3313.54, 6360.33, 7894.06]
sa_best  = [3189.66, 3313.54, 6268.84, 7929.46]

# Plot 1: Runtime vs n
plt.figure()
plt.plot(n, aco_runtime, marker='o', label='ACO')
plt.plot(n, sa_runtime, marker='o', label='SA')
plt.xlabel('Number of Cities (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime vs Problem Size')
plt.legend()
plt.grid(True)
plt.savefig('runtime_vs_n.png')

# Plot 2: Best Tour Length vs n
plt.figure()
plt.plot(n, aco_best, marker='o', label='ACO')
plt.plot(n, sa_best, marker='o', label='SA')
plt.xlabel('Number of Cities (n)')
plt.ylabel('Best Tour Length')
plt.title('Solution Quality vs Problem Size')
plt.legend()
plt.grid(True)
plt.savefig('quality_vs_n.png')

plt.show()
