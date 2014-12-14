# coding:utf-8
class Violence:

    # 暴力搜索: 时间复杂度O(n*n)
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        length = len(num)
        for i in range(0, length):
            for j in range(0, length):
                if (i != j) and (num[i] + num[j] == target):
                    return self.permuteIndex(i + 1, j + 1)

    def permuteIndex(self, i, j):
        maxIndex = i if i > j else j
        minIndex = i if i < j else j
        return (minIndex, maxIndex)


class Hash:

    # Hash解法: 时间复杂度O(n)
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target - x in dict:
                return (dict[target - x] + 1, i + 1)
            dict[x] = i
            print x, target - x, dict
