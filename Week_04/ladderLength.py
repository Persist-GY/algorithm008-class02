# 
from collections import defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList  or endWord not in wordList:
            return 0
        # 保存查看过的单词
        vistited = {}
        # 保存所有匹配 单个* 的结果
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                dic[word[:i] + '*' + word[i+1:]].append(word)
        queue = [(beginWord, 1), ]
        while queue:
            current_word, level = queue.pop(0)
            level += 1
            for i in range(len(current_word)):
                for word in dic[current_word[:i] + '*' + current_word[i+1:]]:
                    if word == endWord:
                        return level
                    if word not in vistited:
                        vistited[word] = True
                        queue.append((word, level))
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList  or endWord not in wordList:
            return 0
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                dic[word[:i]+'*'+word[i+1:]].append(word)
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        visited_begin = {beginWord:1}
        visited_end = {endWord:1}
        def helper(queue, visited, other_visited):
            current_word, level = queue.pop(0)
            for i in range(len(current_word)):
                for word in dic[current_word[:i]+'*'+current_word[i+1:]]:
                    if word in other_visited:
                        return level + other_visited[word]
                    if word not in visited:
                        visited[word]  = level + 1
                        queue.append((word, level + 1))

        while queue_begin and queue_end:
            ans = helper(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = helper(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0
                    




