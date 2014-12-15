# coding:utf-8
import time


def rotateBinarySearch(A, n, key):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) / 2
        print left, right
        if A[mid] == key:
            return mid
        if A[left] <= A[mid]:
            if A[left] <= key and key < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if A[mid] < key and key < A[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    # a = [i for i in range(300, 100000)] + [j for j in range(30)]
    a = [i for i in range(10000000)]
    key = 3234
    starttime = time.time()
    index = rotateBinarySearch(a, len(a), key)
    endtime = time.time()
    print 'list:', 'key =', key, 'index=', index
    print '运行时间', endtime - starttime, 'ms'
