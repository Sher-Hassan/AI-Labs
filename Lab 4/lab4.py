import abc 
from typing import List, Dict, TypeVar, Set 
import numpy as np 
from collections import deque 

NodeToken = TypeVar("NodeToken") 
GraphMapping = Dict[NodeToken, List[NodeToken]] 

class BaseGraph(abc.ABC): 
    def __init__(self, n: int, directed: bool = False) -> None: 
        self.n = n 
        self.directed = directed 
 
    @abc.abstractmethod 
    def add(self, src: int, dst: int, w: int = 1) -> None: 
        raise NotImplementedError 
 
    @abc.abstractmethod 
    def neighbors(self, u: int) -> List[int]: 
        raise NotImplementedError 
 
    @abc.abstractmethod 
    def indeg(self, u: int) -> int: 
        raise NotImplementedError 
 
    @abc.abstractmethod 
    def cost(self, src: int, dst: int) -> float: 
        raise NotImplementedError 
 
    @abc.abstractmethod 
    def show(self) -> None: 
        raise NotImplementedError 
 
class AdjacencyMatrixGraph(BaseGraph): 
    def __init__(self, n: int, directed: bool = False) -> None: 
        super().__init__(n, directed) 
        self.m = np.zeros((n, n), dtype=float) 
 
    def add(self, src: int, dst: int, w: int = 1) -> None: 
        if src < 0 or dst < 0 or src >= self.n or dst >= self.n: 
            raise ValueError(f"Nodes {src} and {dst} are out of bounds") 
        if w < 1: 
            raise ValueError("Edge weight cannot be < 1") 
        self.m[src][dst] = w 
        if not self.directed: 
            self.m[dst][src] = w 
 
    def neighbors(self, u: int) -> List[int]: 
        if u < 0 or u >= self.n: 
            raise ValueError(f"Cannot access node {u}") 
        return [i for i in range(self.n) if self.m[u][i] > 0] 
 
    def indeg(self, u: int) -> int: 
        if u < 0 or u >= self.n: 
            raise ValueError(f"Cannot access node {u}") 
        return sum(1 for i in range(self.n) if self.m[i][u] > 0) 
 
    def cost(self, src: int, dst: int) -> float: 
        if src < 0 or dst < 0 or src >= self.n or dst >= self.n: 
            raise ValueError(f"Nodes {src} and {dst} are out of bounds") 
        return float(self.m[src][dst]) 
 
    def show(self) -> None: 
        for i in range(self.n): 
            for v in self.neighbors(i): 
                print(i, "-->", v) 
 
def bfs(g: GraphMapping, s: NodeToken) -> List[NodeToken]: 
    if s not in g: 
        raise ValueError(f"Start node {s!r} not found") 
    vis: Set[NodeToken] = {s} 
    res: List[NodeToken] = [] 
    q = deque([s]) 
    while q: 
        u = q.popleft() 
        res.append(u) 
        for v in g.get(u, []): 
            if v not in vis: 
                vis.add(v) 
                q.append(v) 
    return res 
 
def dfs(g: GraphMapping, s: NodeToken) -> List[NodeToken]: 
    if s not in g: 
        raise ValueError(f"Start node {s!r} not found") 
    vis: Set[NodeToken] = set() 
    res: List[NodeToken] = [] 
    def go(u: NodeToken) -> None: 
        vis.add(u) 
        res.append(u) 
        for v in g.get(u, []): 
            if v not in vis: 
                go(v) 
    go(s) 
    return res 
 
if __name__ == "__main__": 
    g = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []} 
    print("BFS:", bfs(g, "A"))  
    print("DFS:", dfs(g, "A"))
