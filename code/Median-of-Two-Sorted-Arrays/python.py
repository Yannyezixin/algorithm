# coding:utf-8


class Solution:
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


if __name__ == "__main__":
    a = [1, 12, 4]
    b = [2, 3, 5, 7, 9]
    solu = Solution()
    value = solu.findMedianSortedArrays(a, b)
    print value
