
with open("/Users/sajede/Downloads/rosalind_edta (6).txt", "r") as f:
    s = f.read().splitlines()

string_1 = s[1]
string_2 = s[3]


matrix = []

for i in range(len(string_1) + 1):
    submatrix = []
    for j in range(len(string_2) + 1):
        submatrix.append(0)
    matrix.append(submatrix)
for i in range(len(string_1) + 1):
    matrix[i][0] = i
    for j in range(len(string_2) + 1):
        matrix[0][j] = j

for i in range(1, len(string_1)+1):
    for j in range(1, len(string_2)+1):
        if string_1[i - 1] == string_2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1]
        else:
            matrix[i][j] = 1 + min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1]) #Edit Distance


def getTraceback(sizex, sizey):
    mattarce = []

    for i in range(len(sizex) + 1):
        submattrace = []
        for j in range(len(sizey) + 1):
            submattrace.append(0)
        mattarce.append(submattrace)

    for i in range(1, len(sizex) + 1):
        mattarce[i][0] = 'up'
    for j in range(1, len(sizey) + 1):
        mattarce[0][j] = 'left'

    mattarce[0][0] = 'done'
    return mattarce



traceBack = getTraceback(string_1, string_2)
mat_align = []

for i in range(len(string_1) + 1):
    Submit_align = []
    for j in range(len(string_2) + 1):
        Submit_align.append(0)
    mat_align.append(Submit_align)

for i in range(len(string_1) + 1):
    mat_align[i][0] = i * -1
    for j in range(len(string_2) + 1):
        mat_align[0][j] = j * -1

for i in range(1, len(string_1)+1):
    for j in range(1, len(string_2)+1):
        if string_1[i - 1] == string_2[j - 1]:
            mat_align[i][j] = mat_align[i - 1][j - 1]
            grid_match = mat_align[i][j]
            traceBack[i][j] = 'grid_match'
        else:
            grid_mis = mat_align[i-1][j-1]
            left = mat_align[i][j-1]
            up = mat_align[i-1][j]
            select = max(grid_mis, left, up)
            if select == grid_mis:
                mat_align[i][j] = select - 1
                traceBack[i][j] = 'grid_mis'
            elif select == left:
                mat_align[i][j] = select - 1
                traceBack[i][j] = 'left'
            elif select == up:
                mat_align[i][j] = select - 1
                traceBack[i][j] = 'up'

x_seq = []
y_seq = []

while i > 0 or j > 0:
    if traceBack[i][j] == 'grid_match':
        x_seq.append(string_1[i - 1])
        y_seq.append((string_2[j - 1]))
        i = i - 1
        j = j - 1
    elif traceBack[i][j] == 'grid_mis':
        x_seq.append(string_1[i - 1])
        y_seq.append((string_2[j - 1]))
        i = i - 1
        j = j - 1
    elif traceBack[i][j] == 'left':
        x_seq.append("-")
        y_seq.append(string_2[j - 1])
        j = j - 1
    elif traceBack[i][j] == 'up':
        x_seq.append(string_1[i - 1])
        y_seq.append('-')
        i = i - 1
    else:
        break

x_seq.reverse()
y_seq.reverse()

fin_1 = "".join(x_seq)
fin_2 = "".join(y_seq)

outF = open('myOutFile_1.txt', 'w')
outF.write("%s \n%s \n %s" % (matrix[-1][-1], fin_1, fin_2))