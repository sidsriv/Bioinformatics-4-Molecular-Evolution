import sys

filename = sys.argv[1]

with open(filename) as file:
    data = []
    for line in file:
        data.append(line[:-1])

spec = map(int,data[0].split(' '))
spec.insert(0,0)
proteome = data[1]

def mass(seq):
    m = 0
    for lett in seq:
        m += amino_to_mass[lett]
    return m


def prefix_spec(seq):
    vect = list()
    for i in range(1, len(seq)+2):
        vect.append(mass(seq[:i]))
    return vect


def scorer(seq, spectrum):
    if mass(seq) != len(spectrum)-1:
        return float("-inf")
    else:
        ts = 0
        vector = prefix_spec(seq)
        for pre in vector:
            ts += spectrum[pre]
        return ts

if __name__ == '__main__':
    with open('integer_mass_table.txt') as e:
        mass_to_amino = dict()
        amino_to_mass = dict()
        for item in e:
            temp = item.strip().split(' ')
            try:
                mass_to_amino[int(temp[1])] = temp[0]
                amino_to_mass[temp[0]] = int(temp[1])
            except IndexError:
                pass

    min_pep_l = int((len(spec)-1) / 186) + 1
    max_pep_l = int((len(spec)-1) / 57)

    best_s = 0
    best_p = ''

    for ll in range(min_pep_l, max_pep_l+1):
        for index in range(len(proteome)-ll):
            pep = proteome[index:index+ll]
            s = scorer(pep, spec)
            if s > best_s:
                best_s = s
                best_p = pep
    print(best_s, best_p)