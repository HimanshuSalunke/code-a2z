from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, src):
        visited = [False]*self.n
        order = []
        q = deque([src])
        visited[src] = True
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order

    def dfs(self, src):
        visited = [False]*self.n
        order = []
        stack = [src]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            order.append(u)
            for v in reversed(self.adj[u]):
                if not visited[v]:
                    stack.append(v)
        return order

    def connected_components(self):
        visited = [False]*self.n
        comps = []
        for i in range(self.n):
            if not visited[i]:
                comp = []
                stack = [i]
                while stack:
                    u = stack.pop()
                    if visited[u]:
                        continue
                    visited[u] = True
                    comp.append(u)
                    for v in self.adj[u]:
                        if not visited[v]:
                            stack.append(v)
                comps.append(comp)
        return comps

def main():
    g = Graph(7)
    edges = [(0,1),(0,2),(1,3),(4,5),(5,6)]
    for u,v in edges:
        g.add_edge(u,v)
    print("BFS from 0", g.bfs(0))
    print("DFS from 0", g.dfs(0))
    print("Connected components", g.connected_components())

if __name__ == "__main__":
    main()
