# 下标从0开始
def insertion_sort(a, n):
    for i in range(1, n):
        key = a[i] #从1开始拿元素
        j = i - 1 #找i前面的所有数
        while j >= 0 and a[j] > key: # 直到找到一个比他i的数
            a[j + 1] = a[j] #往后移数
            j -= 1 # 持续往前
        a[j + 1] = key # 填入
