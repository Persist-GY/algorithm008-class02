# https://leetcode-cn.com/problems/minimum-genetic-mutation/

# 队列 一个个字母替换，加到队列里，每次先小循环level + 1 再大循环

class Solution():

    def minMutation(self, start, end, bank):
        if start == end:
            return 0
        genes = ['A', 'C', 'G', 'T']
        level = 0
        queue = [start]
        while queue:
            size = len(queue)
            while size > 0:
                curr = queue.pop()
                if curr == end:
                    return level
                arrCurr = list(curr)
                for i, v in enumerate(arrCurr):
                    for jv in genes:
                        if v != jv:
                            arrCurr[i] = jv
                            strCurr = ''.join(arrCurr)
                            if strCurr in bank:
                                bank.remove(strCurr)
                                queue.insert(0, strCurr)
                    arrCurr[i] = v
                size -= 1
            level += 1
        return -1




