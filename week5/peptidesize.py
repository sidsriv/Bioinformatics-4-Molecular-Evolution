import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

spec = map(int,data[0].split(' '))
spec.insert(0,0)
threshold = int(data[1])
max_score = int(data[2])

def calc_size(i, j):
    s = 0
    new_t = j - spec[i]
    if new_t < 0 or new_t > max_score:
        return s
    for aa in [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]:
        if i - aa >= 0:
            s += sizes[i-aa][new_t]
    return s

if __name__ == '__main__':
    mass = len(spec) - 1
    sizes = [[0 for _ in range(max_score+1)] for __ in range(mass+1)]
    sizes[0][0] = 1
    for i in range(1, mass+1):
        for j in range(1, max_score+1):
            sizes[i][j] = calc_size(i, j)
    total = sum(sizes[mass][threshold:max_score])
    print(total)