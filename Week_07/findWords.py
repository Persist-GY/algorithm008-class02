# https://leetcode-cn.com/problems/word-search-ii/

class Solution():
    if not words or not board: return []
        m = len(board)
        n = len(board[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        res = set()
        # 字典树
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node.setdefault('#','#')

        # DFS
        def search(i, j, curword, curdic):
            if '#' in curdic:
                res.add(curword)
            temp, board[i][j] = board[i][j], '@'
            for d in range(4):
                x, y = i+dx[d], j+dy[d]
                if  0<=x<m and 0<=y<n and board[x][y] in curdic and board[x][y] != '@':
                    search(x, y, curword+board[x][y], curdic[board[x][y]])
            board[i][j] = temp
        
        # 遍历键盘
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    # 递归是否能搜索出单词
                    search(i, j, board[i][j], trie[board[i][j]])
        return list(res)