import numpy as np
from Bio.SubsMat.MatrixInfo import blosum62 as bs62


def read_input(path):
    seqs = []

    with open(path) as f:
        for line in f:
            if line.startswith('>'):
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    return seqs


def blosum62():
    b = bs62.copy()
    for (i, j), v in bs62.items():
        b[(j, i)] = v

    return b


def global_alignment(s, t, scores, gap, gap_e):
    shape = (len(s) + 1, len(t) + 1)
    s_m = np.zeros(shape)
    s_x = np.zeros(shape)
    s_y = np.zeros(shape)

    backtrack_m = np.zeros(shape)
    backtrack_x = np.zeros(shape)
    backtrack_y = np.zeros(shape)

    for i in range(1, len(s) + 1):
        s_m[i][0] = gap + gap_e * (i - 1)
        s_x[i][0] = -9999
        s_y[i][0] = -9999
    for j in range(1, len(t) + 1):
        s_m[0][j] = gap + gap_e * (j - 1)
        s_x[0][j] = -9999
        s_y[0][j] = -9999

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            direction, score = max(enumerate([s_m[i - 1][j] + gap,
                                              s_x[i - 1][j] + gap_e]),
                                   key=lambda x: x[1])
            s_x[i][j] = score
            backtrack_x[i][j] = direction

            direction, score = max(enumerate([s_m[i][j - 1] + gap,
                                              s_y[i][j - 1] + gap_e]),
                                   key=lambda x: x[1])
            s_y[i][j] = score
            backtrack_y[i][j] = direction

            direction, score = max(
                enumerate([s_m[i - 1][j - 1] + scores[(s[i - 1], t[j - 1])],
                           s_x[i][j],
                           s_y[i][j]]), key=lambda x: x[1])
            s_m[i][j] = score
            backtrack_m[i][j] = direction

    s_align, t_align = s, t
    backtrack, max_score = max(enumerate([s_x[i][j], s_y[i][j], s_m[i][j]]),
                               key=lambda x: x[1])
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if backtrack == 0:
            if backtrack_x[i][j] == 0:
                backtrack = 2
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]

        elif backtrack == 1:
            if backtrack_y[i][j] == 0:
                backtrack = 2
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]

        elif backtrack == 2:
            if backtrack_m[i][j] == 1:
                backtrack = 0
            elif backtrack_m[i][j] == 2:
                backtrack = 1
            else:
                i -= 1
                j -= 1

    for remaining in range(i):
        t_align = t_align[:0] + '-' + t_align[0:]
    for remaining in range(j):
        s_align = s_align[:0] + '-' + s_align[0:]

    return str(int(max_score)), s_align, t_align


def main():
    s, t = read_input('/Users/sajede/Downloads/rosalind_gaff (8).txt')
    alignments = global_alignment(s, t, blosum62(), -11, -1)

    with open('rosalind_gaff_out.txt', 'w') as f:
        print('\n'.join(alignments), end='', file=f)


if __name__ == '__main__':
    main()