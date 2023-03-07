def MapLastToFirst(bwt):
    firstcol = sorted(bwt)
    map_index = []
    for eachchar in bwt:
        index = firstcol.index(eachchar)
        map_index.append(index)
        firstcol[index] = "#"
    return map_index


def BWMatching(lastcolumn, pattern, last2first):
    top = 0
    bottom = len(lastcolumn) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            last_short = lastcolumn[top: (bottom + 1)]
            if symbol in last_short:
                topIndex = last_short.index(symbol) + top
                lastIndex = len(last_short) - last_short[::-1].index(symbol) + top - 1
                top = last2first[topIndex]
                bottom = last2first[lastIndex]
            else:
                return 0
        else:
            return bottom - top + 1


def main(bwt, samples):
    last2first = MapLastToFirst(bwt)
    num_matchs = []
    for each in samples:
        num_matchs.append(BWMatching(bwt, each, last2first))
    return num_matchs


if __name__ == "__main__":
    inputFile = '/Users/sajede/Downloads/rosalind_ba9l.txt'

    text, patterns = [x.strip() for x in open(inputFile).readlines()]
    patterns = patterns.split()
    # print text, patterns

    OutF = open('rosaind_ba9l_out', 'w')
    OutF.write(" ".join(map(str, main(text, patterns))))
