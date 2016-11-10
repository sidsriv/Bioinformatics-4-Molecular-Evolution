import sys
filename = sys.argv[1]

with open(filename) as file:
	for line in file:
		string = line[:-1]

def aminoacid_mass_dict():
    '''Returns a dictionary that gives mass of amino acid.'''
    with open('integer_mass_table.txt') as input_data:
        masses = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    mass_dict = {}
    for mass in masses:
        mass_dict[mass[0]] = int(mass[1])

    return mass_dict

def peptidevector(peptide):
	mass_dict = aminoacid_mass_dict()
	vector = ''
	for aa in peptide:
		nums = mass_dict[aa]
		vector += '0'*(nums - 1) + '1'
	return vector

if __name__ == '__main__':
	ans = list(peptidevector(string))
	with open('out.txt','w') as g:
		g.write(' '.join(ans))
	print ' '.join(ans)