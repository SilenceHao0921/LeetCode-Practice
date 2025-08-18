#字串方法
def isPalindrome(x:int)->bool:
    if x < 0:# 負數直接排除
        return False
    s = str(x)# 轉成字串
    return s == s[::-1] # 如果正反一樣，回傳 True。
    
#數字方法
def isPalindrome(x:int)->bool:
    if x < 0:# 負數直接排除
        return False
    o1 = x #o1是變數 存放原來的數字
    r1 = 0 #用來放反轉後的數字
    while x > 0 :
        r1 = r1 * 10 + x % 10 # 逐位反轉
        x // 10 
    return r == o1 
    # 比較反轉後和原始數字是否相同