from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # 如果陣列是空的，直接回傳 0
            return 0

        i = 0  # i 指針，指向最後一個唯一元素
        for j in range(1, len(nums)):  # j 從第 2 個元素開始
            if nums[j] != nums[i]:   # 找到新的不重複數字
                i += 1               # 移動 i 到下一個位置
                nums[i] = nums[j]    # 把新數字放到 nums[i]
        return i + 1  # 長度 = i 索引 + 1
nums = [0,0,1,1,1,2,2,3,3,4]