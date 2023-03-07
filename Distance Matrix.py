from numpy import zeros
#from scripts import ReadFASTA

dna_list = []
with open('/Users/sajede/Downloads/rosalind_pdst.txt') as f:
    for line in f:
        if line.startswith('>'):
            dna_list.append('')
        else:
            dna_list[-1] += line.strip()

#dna_list = [fasta[1] for fasta in ReadFASTA('data/rosalind_pdst.txt')]

# All seqences have the same length.
dna_len = len(dna_list[0])

M = zeros((len(dna_list),len(dna_list)))
for i in range(len(dna_list)):
    for j in range(len(dna_list)):

        if i < j:
            for k in range(dna_len):
                if dna_list[i][k] != dna_list[j][k]:
                    M[i][j] += 1.0/dna_len

        elif i > j:
            M[i][j] = M[j][i]

#print(M)
OutF = open('rosalind_Distance_out.txt', 'w')
OutF.write(' '.join(map(str,M[0])))
for row in range(1, len(dna_list)):
    OutF.write('\n'+(' '.join(map(str, M[row]))))