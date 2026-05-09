def load_hospitals(filename):
    hospitals = []
    with open(filename, "r") as f:
        content = f.read().split()
        n = int(content[0]) 
        for i in range(1, len(content), 3):
            if len(hospitals) < n:
                x = float(content[i+1])
                y = float(content[i+2])
                hospitals.append((x, y))
    return hospitals