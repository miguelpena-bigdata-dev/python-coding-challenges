class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()
        current, left, right = 0, 0, 0
        while (left < m and right < n):
            if nums1_copy[left] <= nums2[right]:
                nums1[current] = nums1_copy[left]
                current += 1
                left += 1
            else:
                nums1[current] = nums2[right]
                current += 1
                right += 1
        
        if left < m:
            while (left < m):
                nums1[current] = nums1_copy[left]
                current+=1
                left += 1
        elif right < n:
            while (right < n):
                nums1[current] = nums2[right]
                current+=1
                right += 1

def main():
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    main()