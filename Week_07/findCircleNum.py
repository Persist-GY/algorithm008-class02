# https://leetcode-cn.com/problems/friend-circles/

from typing import List

class Solution():
    def findCircleNum(self, M: List[List[int]]) -> int:
        level = 0
        m = len(M)
        visted = set()
        def DFS(i):
            for j in range(m):
                if M[i][j] == 1 and j not in visted:
                    visted.add(j)
                    DFS(j)

        for i in range(m):
            if i not in visted:
                level += 1
                DFS(i)
        return level

    # 并查集
    def findCircleNum2(self, M: List[List[int]]) -> int:
        m = len(M)
        p = [i for i in range(m)]
        def parent(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i
                i = p[i]
                p[x] = root
            return root
        def union(p, i, j):
            p1 = parent(p, i)
            p2 = parent(p, j)
            p[p2] = p1
        for i in range(m):
            for j in range(m):
                if M[i][j] == 1:
                    union(p, i, j)
        return len(set([parent(p, i) for i in range(m)]))