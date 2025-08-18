#雙迴圈解法
def twosum (nums,target):
    # 外層迴圈，遍歷每個元素
    for i in range(len(nums)):
        # 內層迴圈，遍歷 i 後面的元素。避免重複（不會檢查相同元素，且不會重複組合）。
        for j in range(i+1,len(nums)):
            # 檢查兩數和是否等於 target
            if nums[i] + nums[j] ==target:
                return [i,j]
print(twosum([2, 7, 11, 15], 9))


#哈希表
def twosum (nums,target):
    #用字典存每個數字：鍵是數字，值是它的索引。
    seen={}
    #逐一遍歷數字和索引。
    for i , n in enumerate(nums):
        #計算需要的另一個數字是多少。
        d = target - n
        #如果這個需要的數字之前出現過，就找到答案。
        if d in seen :
            #回傳之前出現的索引和現在的索引。
            return [seen[d],i]
            #沒找到的話，把目前數字存進字典。
        seen[n] = i
print(twosum([2, 7, 11, 15], 9))