# coding:utf-8


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxP = A[0]
        minP = A[0]
        result = A[0]
        for i in range(1, len(A)):
            maxP_ = maxP
            maxP = max(max(maxP * A[i], A[i]), minP * A[i])
            minP = min(min(maxP_ * A[i], A[i]), minP * A[i])
            result = max(result, maxP)
            print result, maxP, minP, A[i]
        return result


if __name__ == "__main__":
    testOne = [2, 3, -4, -5, 0, 9, 10, -1, -2]
    solu = Solution()
    largestProduct = solu.maxProduct(testOne)

    print largestProduct
