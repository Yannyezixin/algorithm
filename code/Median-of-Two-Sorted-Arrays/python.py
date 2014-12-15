# coding:utf-8
import time


class Solution:

    # 思路：两数组merge后再排序取得中值
    # @return a float
    def findMedianSortedArrays(self, A, B):
        Blen = len(B)
        Alen = len(A)
        Bdict = {}
        for i in xrange(Blen):
            Bdict[i] = B[i]
        for j in range(Blen, Alen + Blen):
            Bdict[j] = A[j - Blen]
        median = sorted(Bdict.values())
        mLen = len(median)
        value = float(median[mLen/2]) if mLen % 2 != 0 else \
            float(median[mLen/2 - 1] + median[mLen/2])/2

        return value

    # 思路：变体二分查找思想。将在范围外的数值删除掉
    # @return int
    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)


if __name__ == "__main__":
    a = [i for i in range(10000) if i % 2 == 0]
    b = [i for i in range(10000) if i % 3 == 0]
    solu = Solution()

    print 'start...'
    starttime = time.time()
    value = solu.findMedianSortedArrays(a, b)
    endtime = time.time()
    print endtime - starttime, 's'

    lenA = len(a)
    lenB = len(b)
    mid = (lenA + lenB)/2
    starttime = time.time()
    if mid % 2 == 0:
        binarySearch = float(solu.getKth(a, b, mid))
    else:
        binarySearch = (solu.getKth(a, b, mid) + solu.getKth(a, b, mid + 1)) * 0.5
    endtime = time.time()
    print endtime - starttime, 'ms'

    print value, binarySearch
