

# 冒泡排序
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            # 相邻两个元素对比 交换
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 选择排序
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    return arr

# 插入排序
def insertionSort(arr):
    n = len(arr)
    preIndex, current = 0, 0
    for i in range(1, n):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and current < arr[preIndex]:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr

# 归并排序
def mergeSort(arr):
    n = len(arr)
    def DFS(begin, end):
        if begin >= end: return
        mid = (begin + end) >> 1
        DFS(begin, mid)
        DFS(mid+1, end)
        cache = [0]*(end-begin+1)
        s, c = begin, 0
        for e in range(mid+1, end+1):
            while s <= mid and arr[s] < arr[e]:
                cache[c] = arr[s]
                s += 1
                c += 1
            cache[c] = arr[e]
            c += 1
        while s <= mid:
            cache[c] = arr[s]
            c += 1
            s += 1
        arr[begin, end+1] = cache
    DFS(0, n-1)
    return arr

# 快速排序
def quickSort(arr):
    def DFS(begin, end):
        def partition(s, e):
            pivot = e
            counter = s
            for i in range(s, e):
                if arr[i] < arr[pivot]:
                    arr[i], arr[counter] = arr[counter], arr[i]
                    counter += 1
            arr[counter], arr[pivot] = arr[pivot], arr[counter]
            return counter
        pivot = partition(begin, end)
        DFS(begin, pivot-1)
        DFS(pivot+1, end)
    DFS(0, len(arr)-1)
    return arr

