
class Cluster(object):
    def __init__(self, id, age, nodes):
        self.id = id
        self.age = age
        self.nodes = nodes

    def compute_distance_with_cluster(self, cluster, distanceMatrix):
        distanceSum = sum(distanceMatrix[i][j] for i in self.nodes for j in cluster.nodes)
        return distanceSum / float(len(self.nodes) * len(cluster.nodes))


def merge_clusters(c1, c2, id, age):
    return Cluster(id, age, c1.nodes + c2.nodes)


def find_closest_clusters(clusterList, clusters, distanceMatrix):
    c1, c2 = min([(c1, c2) for c1 in clusters for c2 in clusters if c1 != c2],
                 key=lambda tup: clusterList[tup[0]].compute_distance_with_cluster(clusterList[tup[1]], distanceMatrix))
    return clusterList[c1], clusterList[c2]


def connect_nodes(graph, parent, child):
    distance = parent.age - child.age
    graph[parent.id].append((child.id, distance))
    graph[child.id].append((parent.id, distance))


def update_distance_matrix(newCluster, clusterList, distanceMatrix):
    distances = [newCluster.compute_distance_with_cluster(cluster, distanceMatrix) for cluster in clusterList]

    for i in range(len(distanceMatrix)):
        distanceMatrix[i].append(distances[i])

    distanceMatrix.append(distances + [0])


def upgma(distanceMatrix, n):

    from collections import defaultdict

    clusterList = [Cluster(id, age=0, nodes=[id]) for id in range(n)]
    clusters = set([id for id in range(n)])
    graph = defaultdict(list)
    currentId = n

    while len(clusters) > 1:
        c1, c2 = find_closest_clusters(clusterList, clusters, distanceMatrix)

        age = c1.compute_distance_with_cluster(c2, distanceMatrix) / 2

        newCluster = merge_clusters(c1, c2, currentId, age=age)
        currentId += 1

        connect_nodes(graph, newCluster, c1)
        connect_nodes(graph, newCluster, c2)

        clusters.remove(c1.id)
        clusters.remove(c2.id)
        clusters.add(newCluster.id)
        clusterList.append(newCluster)

        update_distance_matrix(newCluster, clusterList, distanceMatrix)

    return graph


if __name__ == '__main__':
    with open('/Users/sajede/Downloads/rosalind_ba7d (1).txt') as file:
        n = int(file.readline())
        distanceMatrix = [list(map(int, file.readline().split())) for _ in range(n)]

        T = upgma(distanceMatrix, n)

    with open('/Users/sajede/Downloads/rosalind_ba7d_out.txt', 'w') as outFile:
        nodeCount = len(T)
        for u in range(nodeCount):
            for v, w in T[u]:
                print('%d->%d:%.3f' % (u, v, w), file=outFile)