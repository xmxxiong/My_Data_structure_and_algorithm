# 汉诺塔问题(递归)
def hano(n, a, b, c):
    if n > 0:
        hano(n-1, a, c, b)
        print('moving from {} to {}'.format(a, c))
        hano(n-1, b, a, c)

############## 查找 ##############

# 线性查找o(n)
def linear_search(lis, val):
    for index, val in enumerate(lis):
        if val == lis[index]:
            return index
    else: 
        return None

# 二分查找o(logn)
def binary_search(lis, val):
    left = 0
    right = len(lis) -1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == val:
            return mid
        elif lis[mid] < val:
            left  = mid + 1
        else:
            right = mid - 1
    else:
        return None
        

############## 排序 ##############
# 冒泡排序1
import random
def bubble_sort1(lis):
    for i in range(len(lis) -1):
        for j in range(len(lis)-i -1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1] , lis[j]
    return lis

# 冒泡排序2(优化点：若存在一趟没有进行元素交换，则表示排序已经结束)
import random
def bubble_sort2(lis):
    for i in range(len(lis) -1):
        flag = False
        for j in range(len(lis)-i -1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1] , lis[j]
                flag = True
        if flag == False:
            return lis


# 选择排序1(o(n^2))
def select_sort1(lis):
    result = []
    for i in range(lis):
        min_val = min(lis)  # 该操作是o(n)
        result.append(min_val)
        lis.remove(min_val)
    return result


# 选择排序2(o(n^2),优化项:降低了空间复杂度)
def select_sort2(lis):
    for i in range(len(lis)-1):
        min_val = i
        for j in range(i+1, len(lis)):
            if lis[min_val] > lis[j]:
                min_val = j
        lis[i], lis[min_val] = lis[min_val], lis[i]
    return lis

# 插入排序(o(n^2))
def insert_sort(lis):
    for i in range(1, len(lis)): # i 表示取出元素的下标
        j = i - 1
        tmp = lis[i]
        while lis[j] > lis[i]  and j >= 0:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = tmp
    return lis

    
# 快速排序(复杂度：nlog(n))
def quick_sort(lis, left, right):
    if left < right:
        mid = patition(lis, left, right)
        quick_sort(lis, left, mid-1)
        quick_sort(lis, mid+1, right)
    return lis

def patition(lis, left, right):
    tmp = lis[left]
    while left < right:
        while lis[right] >= tmp and left < right:
            right -= 1
        lis[left] = left[right]
        while lis[left] <= tmp and left < right:
            left += 1
        lis[right] = left[left]
    lis[left] = tmp
    return left
        
# 堆排序·















































