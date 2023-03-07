with open('/Users/sajede/Downloads/rosalind_ba7b (1).txt') as f:
    Read = (f.read().splitlines())


n = int(Read[0])
j = int(Read[1])

Dis_Mat = []
for i in range(0, n):
    Sub_mat = []
    for k in range(0, n):
        Sub_mat.append(0)
    Dis_Mat.append(Sub_mat)

for i in range(0, n):
    d = Read[i + 2].split()
    for k in range(0, n):
        Dis_Mat[i][k] = int(d[k])


if j > 0:
    i = j - 1
else:
    i = j + 1

Limb_Leaf = int('10000')
for k in range(0, n):
    if k != i and k != j:
        Length = (Dis_Mat[j][i] + Dis_Mat[j][k] - Dis_Mat[i][k]) / 2
        if Length < Limb_Leaf:
            Limb_Leaf = Length

OutF = open('rosalind_ba7b_out.txt', 'w')
OutF.write(str(int(Limb_Leaf)))