# coding:utf-8


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        largestSum = -2147483648
        currentSum = 0
        for i in range(len(A)):
            currentSum += A[i]
            if largestSum < currentSum:
                largestSum = currentSum
            else:
                currentSum = 0
        return largestSum
