class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            target = -1 * nums[i]

            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return output