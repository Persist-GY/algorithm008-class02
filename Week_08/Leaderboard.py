# https://leetcode-cn.com/problems/design-a-leaderboard/

class Leaderboard:

    def __init__(self):
        self.board = []

    def quickSort(self, begin, end):
        # 快速排序
        if begin >= end: return
        def partition(s, e):
            pivot = e
            counter = s
            for i in range(s, e):
                sore = self.board[i][1]
                if sore > self.board[pivot][1]:
                    self.board[counter], self.board[i] = self.board[i], self.board[counter]
                    counter+=1
            self.board[counter], self.board[pivot] = self.board[pivot], self.board[counter]
            return counter
        pivot = partition(begin, end)
        self.quickSort(begin, pivot-1)
        self.quickSort(pivot+1, end)

    def addScore(self, playerId: int, score: int) -> None:
        exist = False
        for i in range(len(self.board)):
            d, s = self.board[i]
            if d == playerId:
                self.board[i][1] = s + score
                exist = True
        if not exist:
            self.board.append([playerId, score])
       
        

    def top(self, K: int) -> int:
         # 排序根据分数
        self.quickSort(0, len(self.board)-1) 
        res = 0
        for i in range(K):
            res += self.board[i][1]
        return res

    def reset(self, playerId: int) -> None:
        for arr in self.board:
            d, s = arr
            if d == playerId:
                self.board.remove(arr)
                break
        self.board.append([playerId, 0])


class Leaderboard3:

    def __init__(self):
        self.dic = {}
        
    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] = self.dic.get(playerId, 0) + score

    def top(self, K: int) -> int:
        s = sorted([v for v in self.dic.values()], reverse = True)
        return sum(s[:K])
        
    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0

class Leaderboard:

    def __init__(self):
        self.dic = {}

    def quickSort(self, arr, begin, end):
        if begin >= end: return
        def partition(s, e):
            pivot = e
            counter = s
            for i in range(s, e):
                if arr[i] > arr[pivot]:
                    arr[counter], arr[i] = arr[i], arr[counter]
                    counter+=1
            arr[counter], arr[pivot] = arr[pivot], arr[counter]
            return counter
        pivot = partition(begin, end)
        self.quickSort(arr, begin, pivot-1)
        self.quickSort(arr, pivot+1, end)

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] = self.dic.get(playerId, 0) + score
       
    def top(self, K: int) -> int:
        arr = []
        for key, v in self.dic.items():
            arr.append(v)
        print(self.dic)
        # 排序根据分数
        self.quickSort(arr, 0, len(arr)-1) 
        res = 0
        for i in range(K):
            res += arr[i]
        return res

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0
