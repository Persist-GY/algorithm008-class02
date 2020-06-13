# https://leetcode-cn.com/problems/n-queens-ii/

class Solution():

    def totalNQueens(self, n):
        self.count = 0
        def DFS(row, col, pie, na):
            if row == n: 
                self.count += 1 
                return
            bits = (~(col|pie|na))&((1<<n)-1) # 最高位到第n位 清0
            while bits:
                queen = bits & -bits # 获取最低位1   皇后
                DFS(row+1, col|queen, (pie|queen)<<1, (na|queen)>>1) # 进行下一层递推
                bits = bits & (bits-1) # 最低位1清0 清除皇后
        DFS(0, 0, 0, 0)
        return self.count