# https://leetcode-cn.com/problems/surrounded-regions/

class Solution():

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return board
        m = len(board)
        n = len(board[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        def DFS(i, j):
            board[i][j] = 'B'
            for c in range(4):
                if 0<i+dx[c]<m-1 and 0<j+dy[c]<n-1 and board[i+dx[c]][j+dy[c]] == 'O':
                    DFS(i+dx[c], j+dy[c])

        for i in range(n):
            # 第一行
            if board[0][i] == 'O':
                DFS(0, i)
            # 最后一行
            if board[m-1][i] == 'O':
                DFS(m-1, i)
        
        for i in range(m):
            # 第一列
            if board[i][0] == 'O':
                DFS(i, 0)
            # 最后一列
            if board[i][n-1] == 'O':
                DFS(i, n-1)
        print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = "O"
        return board
