from Bio import SeqIO

Data_list = []
with open("/Users/sajede/Downloads/rosalind_corr (3).txt") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        Data_list.append(str(record.seq))

def revers_complt(rec_seq):
    revers_word = list(rec_seq)
    revers_word.reverse()
    complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}
    for i in range(0, len(revers_word)):
        revers_word[i] = complementDict[revers_word[i]]
    fine_revers = "".join(revers_word)
    return fine_revers


full_dict = {}
for letter in Data_list:
    full_dict[letter] = full_dict.get(letter, 0) + 1
    rev_letter = revers_complt(letter)
    if rev_letter in Data_list:
        full_dict[letter] += 1

Correct_list = []
Incorrect_list = []
for this_one in list(full_dict.keys()):
    if full_dict[this_one] >= 2:
        Correct_list.append(this_one)
    else:
        Incorrect_list.append(this_one)


def hamming_distance(string1, string2):
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance


Correction = []
for inc in Incorrect_list:
    for cr in Correct_list:
        rev_cr = revers_complt(cr)
        Hamming_dist_1 = hamming_distance(inc, cr)
        Hamming_dist_2 = hamming_distance(inc, rev_cr)
        if Hamming_dist_1 == 1:
            Correction.append((inc, cr))
            break
        elif Hamming_dist_2 == 1:
            Correction.append((inc, rev_cr))

Correct = set(Correction)

for ir, cr in Correct:
    outF = open("OutFile_rosalind_corr.txt", 'a')
    outF.write("{}->{}".format(ir, cr))
    outF.write("\n")