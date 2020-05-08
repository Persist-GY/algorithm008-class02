# https://leetcode-cn.com/problems/n-queens/

# 根据行，遍历每一列，如果本列，撇 那 有皇后那直接到下一列

class Solution():
    
    def solveNQueens(self, n):
        self.n = n
        self.res = []
        self.col = []
        self.pie = []
        self.na = []
        def helper(row, curr_state):
            if row == n:
                self.res.append(curr_state)
                return
            for col in range(n):
                if col in self.col or row + col in self.pie or row - col in self.na:
                    continue
                self.col.append(col)
                self.pie.append(row + col)
                self.na.append(row - col)
                helper(row + 1, curr_state + [col])
                self.col.pop()
                self.pie.pop()
                self.na.pop()
        helper(0, [])
        board = []
        for arr in self.res:
            for i in arr:
                board.append('.'*i+'Q'+'.'*(n-i-1))
        return [board[i:i+n] for i in range(0, len(board), n)]
            