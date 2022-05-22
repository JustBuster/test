class Solution(object):
    def twoSum(self, nums, target):

        hashMap = {} # value: index

        for i, n in enumerate(nums):
            print(f"i : {i}, n : {n}")
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[n] = i
        

