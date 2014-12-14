# coding:utf-8
import time


def binarySearch(A, n, key):
    left = 0
    right = n - 1
    while left <= right:
        # print left, right
        mid = (left + right)/2

        # 程序一开始不应判断相等，数组中不想等的情况更多
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        """
        if A[mid] < key:
            left = mid + 1
        elif A[mid] > key:
            right = mid - 1
        else:
            return mid
        """

    return -1


def binarySearchRecusion(A, left, right, key):
    if left <= right:
        mid = (left + right)/2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid + 1
            return binarySearchRecusion(A, left, right, key)
        else:
            right = mid - 1
            return binarySearchRecusion(A, left, right, key)
    else:
        return -1


def violence(A, n, key):
    if key in A:
        return A.index(key)
    return -1

if __name__ == '__main__':
    a = [i for i in range(10000000)]
    key = 134234

    print '开始二分查找'
    starttimeBin = time.time()
    binary = binarySearch(a, len(a), key)
    endtimeBin = time.time()
    print binary
    print "二分查找:", (endtimeBin - starttimeBin) * 1000, 'ms'

    print '开始二分递归查找'
    starttimeBin = time.time()
    binary = binarySearchRecusion(a, 0, len(a) - 1, key)
    endtimeBin = time.time()
    print binary
    print "二分递归查找:", (endtimeBin - starttimeBin) * 1000, 'ms'

    print '开始暴力查找'
    starttimeVio = time.time()
    vio = violence(a, len(a), key)
    endtimeVio = time.time()
    print vio
    print "暴力查找:", (endtimeVio - starttimeVio) * 1000, 'ms'
