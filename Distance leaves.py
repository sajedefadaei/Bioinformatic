from queue import Queue

with open('/Users/sajede/Downloads/rosalind_ba7a (2).txt') as f:
    Data = (f.read().splitlines())

# print(Read)

n = int(Data[0])
graphDict = {}

for d in Data[1:]:
    part_1 = d.split("->")
    part_2 = part_1[1].split(":")
    if int(part_1[0]) not in graphDict:
        graphDict[int(part_1[0])] = []
    graphDict[int(part_1[0])].append((int(part_2[0]), int(part_2[1])))


# print(graphDict)


def Dis_Matrix(m):
    dis_mat = []
    for k in range(0, m):
        sub_dis = []
        for z in range(0, m):
            sub_dis.append(0)
        dis_mat.append(sub_dis)
    return dis_mat


Dis_mat = Dis_Matrix(n)
for i in range(0, n):
    dist = dict()
    queue = Queue()
    dist[i] = 0
    queue.put(i)
    while not queue.empty():
        curNode = queue.get()
        for node, weight in graphDict[curNode]:
            if not node in dist:
                dist[node] = dist[curNode] + weight
                if node < n:
                    Dis_mat[i][node] = dist[node]
                queue.put(node)

outF = open('rosalind_ba7a', 'w')
for d in Dis_mat:
    outF.write(' '.join([str(i) for i in d]))
    outF.write('\n')