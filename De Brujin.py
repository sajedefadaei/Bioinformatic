inputFilePath = "/Users/sajede/Downloads/rosalind_dbru (3).txt"

with open(inputFilePath) as f:
    Mylist = (f.read().splitlines())
dna_list = list(set(Mylist))
# print(dna_list)

set_second = []
for letter in dna_list:
    cont = list(letter)
    cont.reverse()
    complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}
    for i in range(0, len(cont)):
        cont[i] = complementDict[cont[i]]
    set_second.append("".join(cont))

dna_list.extend(set_second)
dna_listfinal = list(set(dna_list))

graph = {}

for s in dna_listfinal:
    left = s[:-1]
    right = s[1:]
    if left not in graph:
        graph[left] = list(set())
    if right not in graph:
        graph[right] = list(set())
    graph[left].append(right)

outF = open('Rosalind_dbru_out.txt', 'w')
for this_one, key in graph.items():
    if len(key) > 1:
        for i in range(0, len(key)):
            outF.write("(%s , %s)" % (this_one, key[i]))
            outF.write("\n")
    elif len(key) > 0:
        outF.write("(%s , %s)" % (this_one, " ".join(list(key))))
        outF.write("\n")