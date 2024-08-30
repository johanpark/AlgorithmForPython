def build_graph(edges):
    graph = {}
    for (src, dest, weight) in edges:
        if src not in graph:
            graph[src] = {}
        if dest not in graph:
            graph[dest] = {}
        graph[src][dest] = weight
        graph[dest][src] = weight
    return graph


def dfs(graph, start, end):
    visited = set()
    stack = [(start, end)]
    while stack:
        cur, end = stack.pop()
        if cur in visited:
            continue


n = int(input())
m = int(input())

edges = []
for _ in range(m):
    src, dest, weight = map(int, input().split())
    edges.append((src, dest, weight))

start_node, end_node = map(int, input().split())
graph = build_graph(edges)
dfs(graph, start_node, end_node);
