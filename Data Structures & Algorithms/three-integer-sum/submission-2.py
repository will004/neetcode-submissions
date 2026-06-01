class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        output = []
        if (len(nums) < 3):
            return output
        
        for i in range(len(sorted_nums)):
            target = -1 * sorted_nums[i]
            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                current_sum = sorted_nums[j] + sorted_nums[k]

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    if not ([sorted_nums[i], sorted_nums[j], sorted_nums[k]] in output):
                        output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
            
        return output

# target = 4
# [-4, -1, -1, 0, 1, 2]