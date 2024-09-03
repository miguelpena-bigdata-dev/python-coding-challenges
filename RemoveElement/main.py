class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        filtered_nums = list(filter(lambda x: x!=val, nums))
        k = len(filtered_nums)
        for i, num in enumerate(filtered_nums):
            nums[i] = num
            
        return k        


def main():
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    k = solution.removeElement(nums, val)
    print(k)

if __name__ == '__main__':
    main()