import sys
filename = sys.argv[1]

with open(filename) as file:
	for line in file:
		string = line[:-1].split(' ')

def aminoacid_mass_dict():
    '''Returns a dictionary that gives mass of amino acid.'''
    with open('integer_mass_table.txt') as input_data:
        masses = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    mass_dict = {}
    for mass in masses:
        mass_dict[int(mass[1])] = mass[0]

    return mass_dict

def peptideproblem(string):
    endline = len(string)
    pos = 0
    mass_dict = aminoacid_mass_dict()
    peptide = ''
    while pos != endline:
        num = string.index('1',pos)
        peptide += mass_dict[num - pos + 1]
        pos = num + 1
    return peptide


if __name__ == '__main__':
    ans = peptideproblem(string)
    print ans
