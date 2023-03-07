from queue import Queue
with open('/Users/sajede/Downloads/rosalind_ba7c (2).txt') as f:
    Read = (f.read().splitlines())

n = int(Read[0])

Dis_Mat = []
for i in range(0, n):
    Sub_mat = []
    for k in range(0, n):
        Sub_mat.append(0)
    Dis_Mat.append(Sub_mat)

for i in range(0, n):
    d = Read[i + 1].split()
    for k in range(0, n):
        Dis_Mat[i][k] = int(d[k])


def Calculate_Limblengh(D, j, n):
    global currentindex, Length
    if j > 0:
        i = j - 1
    else:
        i = j + 1
    Limb_Leaf = int('10000')
    for k in range(0, n):
        if k != i and k != j:
            Length = (D[j][i] + D[j][k] - D[i][k]) / 2
        if Length < Limb_Leaf:
            Limb_Leaf = int(Length)
            currentindex = (i, k)
    return Limb_Leaf, currentindex[0], currentindex[1]


def Addnode(adj, j, Limblength, i, k, x):
    l = len(adj)
    dist = [int('10000')] * l
    parent = [-1] * l
    queue = Queue()
    dist[i] = 0
    queue.put(i)
    while not queue.empty():
        currentNode = queue.get()
        for node, weight in adj[currentNode].items():
            if int('10000') == dist[node]:
                dist[node] = dist[currentNode] + weight
                parent[node] = currentNode
                queue.put(node)
                if node == k:
                    preNode = node
                    while x < dist[preNode]:
                        currentNode = preNode
                        preNode = parent[currentNode]
                    if x == dist[preNode]:
                        adj[preNode][j] = Limblength
                        adj[j][preNode] = Limblength
                    else:
                        adj.append(dict())
                        Newnode = len(adj) - 1
                        adj[j][Newnode] = Limblength
                        adj[Newnode][j] = Limblength
                        del adj[preNode][currentNode]
                        del adj[currentNode][preNode]
                        adj[preNode][Newnode] = x - dist[preNode]
                        adj[Newnode][preNode] = x - dist[preNode]
                        adj[currentNode][Newnode] = dist[currentNode] - x
                        adj[Newnode][currentNode] = dist[currentNode] - x
                    return



adj = [dict() for _ in range(n)]
adj[0][1] = Dis_Mat[0][1]
adj[1][0] = Dis_Mat[1][0]

for j in range(2, n):
    Limb_length, i, k = Calculate_Limblengh(Dis_Mat, j, j+1)
    x = Dis_Mat[i][j] - Limb_length
    Addnode(adj, j, Limb_length, i, k, x)

OutF = open('rosalind_ba7c_out.txt', 'w')

for i, dicts in enumerate(adj):
    for s, w in dicts.items():
        OutF.write(str(i)+'->'+str(s)+':'+str(w))
        OutF.write('\n')