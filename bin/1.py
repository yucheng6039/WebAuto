#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1:
#
# 输入: [10,2]
# 输出: 210
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
def bi(i):
    if i == 0:
        return 0
    s = 0
    k = i
    while i >= 1  :
        i=i/ 10
        s+=1
    return k /( 10 **s)

class Solution(object):
    def largestNumber(self, nums):
        nums = sorted(nums,key = bi,reverse=True)
        if nums[0] == 0:
            return "0"
        print(nums)
        return "".join([str(i) for i in nums])


S = Solution()
print(S.largestNumber([10,2,34,345,3456]))

