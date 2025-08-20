# 💻 LeetCode-Practice

這個專案紀錄我在練習 **LeetCode 演算法題目** 的解題程式碼與心得，主要使用 **Python**。  
希望透過持續練習，強化邏輯思維與演算法能力。  

---

##  題目清單

###  Easy
1. [Two Sum](./01-Two-Sum.PY)                   
**題目：**
def twosum (nums,target):
給定一個整數陣列 `nums` 和一個目標值 `target`，請你在陣列中找出 **兩個數**，它們的和為 `target`，並回傳它們的 **索引**。
你可以假設 **每種輸入只會對應一個答案**，同一個元素 **不能重複使用**。
你可以以任意順序回傳答案。
可使用雙迴圈,哈希表來解

2. [Palindrome Number](./02-Palindrome-Number.PY)                     
**題目：**
def isPalindrome(x:int)->bool:
給定一個整數 `x`，如果 `x` 是**回文整數**，則回傳 `True`；否則回傳 `False`。
回文數：正著寫和倒著寫相同的數字。

3. [Reverse Integer](./03-Reverse-Integer.PY)                    
**題目：**                 
def rev(x:int)->int:                 
給定一個 32 位元有號整數 `x`，返回將其數字**反轉**後的整數。
**注意：**
如果反轉後的整數超出了 **32 位元有號整數範圍** `[-2^31, 2^31 - 1]`，則回傳 `0`。

4. [Remove Duplicates from Sorted Array](./04-Remove-Duplicates-from-Sorted-Array.PY)             
**題目：**                                 
from typing import List                                       
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                                
給定一個**已排序（非遞減順序）**的整數陣列 `nums`。
你需要**就地 (in-place)** 移除重複元素，使每個元素只出現一次。
函式必須回傳移除後陣列的「新長度」。
額外要求：不可以另外使用額外的陣列空間（O(1) 空間複雜度）。
⚠️ 注意：
雖然函式回傳的是長度，但 `nums` 前半段的元素需要被修改成「不重複的序列」。
###  Medium
（之後會新增）

###  Hard
（之後會新增）

---

##  學習目標
- 熟悉常見演算法（雙指標、哈希表、排序等）  
- 練習寫出 **乾淨、可讀性高** 的程式碼  
- 累積解題思路，提升面試應對能力  

---

## 🚀 未來規劃
- 持續解更多 **Easy / Medium** 題目  
- 整理每題的 **解題思路與註解**  

---
