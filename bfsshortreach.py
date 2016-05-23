from Queue import Queue

testN = int(raw_input())
graphs = {}
roots = {}

for i in range(1, testN + 1):
    graphs[i] = {}
    x, y = map(int, raw_input().split())
    for node in range(1, x + 1):
        graphs[i][node] = []
    for e in range(y):
        n1, n2 = map(int, raw_input().split())
        graphs[i][n1].append(n2)
        graphs[i][n2].append(n1)
    roots[i] = int(raw_input())
    nodes = list(set(graphs[i].keys()))


def BFS(root, graph):
    distances = {}
    for node in graph.keys():
        if node == root:
            distances[node] = 0
        else:
            distances[node] = -1
    q = Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        for node in graph[current]:
            if distances[node] == -1:
                distances[node] = distances[current] + 1
                q.put(node)
    del distances[root]
    for i in distances.keys():
        if distances[i] != -1:
            distances[i] *= 6
    return distances


for i in range(1, len(graphs.keys()) + 1):
    res = ""
    for distance in BFS(roots[i], graphs[i]).values():
        if not res:
            res += str(distance)
        else:
            res = res + " " + str(distance)
    print res
