class Solution(object):
    def search(self, nums, target):

        global h, l
        
        h = len(nums) - 1
        
        l = 0

        def binarySearch(nums, target, low, high):

            high = h

            low = l


            if high >= low:
                mid = (high + low)//2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    binarySearch(nums, target, mid, low)

                elif nums[mid] < target:
                    binarySearch(nums, target, high, mid)

                
            else:

                return -1

            binarySearch(nums, target, l, h)



        