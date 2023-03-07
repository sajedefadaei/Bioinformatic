with open("/Users/sajede/Downloads/rosalind_pcov (5).txt") as f:
    Mylist = (f.read().splitlines())

dna_list = list(set(Mylist))

edge_list = []

for s in dna_list:
    left = s[:-1]
    right = s[1:]
    edge_list.append([left, right])

start = edge_list[0]

k = len(dna_list[0])

first_word = edge_list[0][0]
second_word = edge_list[0][1]
superstring = first_word + second_word[-1]

i = 0
while i < len(dna_list) - k:
    for j in range(len(edge_list)):
        if start[1] == edge_list[j][0]:
            Next = j
            break
    start = edge_list[Next]
    second_word = start[1]
    superstring += second_word[-1]
    i += 1
outF = open('rosalind_pcov_out.txt', 'w')
outF.write(superstring)