# 合并操作：将两个已排序的子数组合并为一个有序数组
def merge(arr, left, mid, right, temp):
    i = left  # 左半部分起始指针
    j = mid + 1  # 右半部分起始指针
    k = left  # temp数组的起始位置

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # 将temp数组中的元素复制回原数组arr中
    for i in range(left, right + 1):
        arr[i] = temp[i]


def merge_sort(arr, left, right, temp):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, temp)  # 排序左半部分
        merge_sort(arr, mid + 1, right, temp)  # 排序右半部分
        merge(arr, left, mid, right, temp)  # 合并左右部分


def main():
    n = int(input())  # 输入数组的大小
    arr = list(map(int, input().split()))  # 输入数组的元素
    temp = [0] * len(arr)  # 创建辅助数组
    merge_sort(arr, 0, n - 1, temp)  # 调用归并排序
    for i in arr:  # 输出排序后的数组
            print(i, end=' ')

if __name__ == "__main__":
    main()
