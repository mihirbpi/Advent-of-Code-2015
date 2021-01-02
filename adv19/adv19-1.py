from aocd import get_data
import re

my_list = get_data(day=19, year=2015).split("\n\n")
replacements = my_list[0].split("\n")
molecule = my_list[1].replace("\n", "")
atoms_set = set()
replacements_dict = {}

for i in range(0, len(replacements)):
    replacement_split = replacements[i].split(" => ")
    atoms_set.add(replacement_split[0])

atoms_list = list(atoms_set)

for atom in atoms_list:
    replacements_dict[atom] = []

for i in range(0, len(replacements)):
    replacement_split = replacements[i].split(" => ")
    replacements_dict[replacement_split[0]].append(replacement_split[1])

def distinct_set(molecule):
    result_set = set()
    molecule_list = re.findall('[A-Z][^A-Z]*', molecule)

    for i in range(0, len(molecule_list)):
        atom = molecule_list[i]

        if(atom in replacements_dict.keys()):

            for replacement in replacements_dict[atom]:
                result_set.add("".join(molecule_list[0:i]) + replacement + "".join(molecule_list[i+1:]))

    return list(result_set)

print(len(distinct_set(molecule)))
