import random
import math

sizes= [20, 50, 100]
max_coord = 1000
def generate_tsp_instance(num_cities, filename):
    with open(filename, "w") as f:
        f.write(f"{num_cities}\n")
        for i in range(num_cities):
            x = random.randint(0, max_coord)
            y = random.randint(0, max_coord)
            f.write(f"{i} {x:.2f} {y:.2f}\n")
    print(f'generated tsp_instances.txt with {num_cities} cities.')

for size in sizes:
    generate_tsp_instance(size, f"tsp_{size}.txt")

generate_tsp_instance(10, "tsp_10_test.txt")

