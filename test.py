import sys
import traceback
"""
基本思路为还是可以抽象为 0 1 背包问题，
只不过对于某种物品，不再仅仅是 选 和 不选，而是
1.不选
2.选主物品
3.选主物品 + 附属1
4.选主物品 + 附属2
...
多种选择方案，也就是基本类似于多重背包问题。
"""
 
try:
    while True:
        """
        items 中的元素格式为，每个 item 为主物品，其中有个属性为附物品，没有附物品的为 null
        """
        mi = {}
        si = {}
        N, m = map(int, input().strip().split())
        for i in range(1, m+1):
            v, p, q = map(int, input().strip().split())
            if q == 0:
                # main item
                mi[i] = [v//10, p]
            else:
                if q in si:
                    si[q].append([v//10, p])
                else:
                    si[q] = [[v//10, p]]

        dp = [0 for _ in range(N//10 + 1)]
        i_keys = list(mi.keys())
        print(i_keys)
        for i in range(len(i_keys)):
            key = i_keys[i]
            for j in range(N//10, -1, -1):#内循环逆序，得到dp[100]~dp[0],最终目标dp[100]
                if j >= mi[key][0]: # 考虑选择主（剩余预算>该主件价格：选择）
                    path2 = dp[j -mi[key][0]] + mi[key][0] * mi[key][1]
                    print(path2)
                    dp[j] = max(dp[j], path2)
                if key not in si: # 考虑 主从
                    pass
                else:
                    if len(si[key]) == 1:#只有一个附件
                        if j >= (mi[key][0] + si[key][0][0]): # 选第一个附件
                            path3 = dp[j - mi[key][0] - si[key][0][0]] + mi[key][0] * mi[key][1] + si[key][0][0] * si[key][0][1]
                            print(path3)
                            dp[j] = max(dp[j], path3)
                    else:
                        if j >= (mi[key][0] + si[key][0][0]): # 选第一个附件（判断预算是否超过主件和第一附件）
                            path4 = dp[j - mi[key][0] - si[key][0][0]] + mi[key][0] * mi[key][1] + si[key][0][0] * si[key][0][1]
                            print(path4)
                            dp[j] = max(dp[j], path4)
                        if j >= (mi[key][0] + si[key][1][0]): # 选第二个附件
                            path5 = dp[j - mi[key][0] - si[key][1][0]] + mi[key][0] * mi[key][1] + si[key][1][0] * si[key][1][1]
                            print(path5)
                            dp[j] = max(dp[j], path5)
                        if j >= (mi[key][0] + si[key][0][0] + si[key][1][0]): # 选第一第二附件
                            path6 = dp[j - mi[key][0] - si[key][0][0] - si[key][1][0]] + mi[key][0] * mi[key][1] + si[key][0][0] * si[key][0][1] + si[key][1][0] * si[key][1][1]
                            print(path6)
                            dp[j] = max(dp[j], path6)
        print(dp[N//10] * 10)#dp[100]*10
        break
except Exception as e:
    traceback.print_exc()