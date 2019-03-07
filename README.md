# Python-Note

## 安裝
基本上一直下一步就好了  
[python3.7.2](https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe)  

## Python 語法基礎
變數(variables)與資料型態、型別(types)  
* 賦予名字給某個值  
* 在程式裡重複使用  
* 值可以不斷被改變  

**變數名稱保留字(不能拿來當變數名稱):**

| and | as | assert | break | class |
| :------| ------: | :------: | :------: | :------: |
| continue | def | del | elif | else |
| except | finally | for | from | global |
| if | import | in | is | lambda |
| not | or | pass | print | raise |
| return | try | while | with | yield |

**指定變數的語法：**

``` python
x = 20  # 代表x等於20,等於不是數學內相等的意思,而是指定,左右不能互換
```

**使用變數：**
``` python
x = 10
y = x * 40    # 結果 y 等於400
```

**基本運算**

| 二元運算子 | 用法 | 說明 |
| :------| ------: | :------: |
| + | X+Y | X加上Y |
| - | X-Y | X減去Y |
| * | X*Y | X乘以Y |
| / | X/Y | X除以Y |
| % | X%Y | 取X除以Y的餘數 | 

``` python
print(5 + 3)    # 8
print(25 - 10)  # 15
print(5 * 3)    # 15
print(10 / 5)   # 2
print(21 % 2)   # 1     21/2 的餘數為 1，所以結果為 1  
print(3 ** 5)   # 243   3 的 5 次方  
```

**比較運算子**

| 關係運算子 | 用法 | 傳回true的條件 |
| :------| ------: | :------: |
| < | X<Y | X小於Y |
| <= | X<=Y | X小於等於Y |
| == | X==Y | X等於Y |
| != | X!=Y | X不等於Y |
| >= | X>=Y | X大於等於Y | 
| > | X>Y | X大於Y | 

``` python
print(2 == 2)  # true
print(2 == 5)  # false
print(3 != 3)  # false
print(3 != 4)  # true

'''
== 和 = 是完全不一樣的
= 用於指定，將左項指定為右項的值，左右不可交換
== 用於比較，比較兩者是否相等，左右可以交換
'''

# 另外比較運算子也可用於字串 
print('word' == 'word')   # true
print('word' != 'world')  # true
```

**邏輯運算子**

| 邏輯運算子 | 用法 | 傳回true的條件 |
| :------| ------: | :------: |
| and | X and Y | X與Y必須同時為true |
| or | X or Y | X與Y之一為true即可 |
| not | not X | X為false |

``` python
print(True and True)   # true
print(True and False)  # false
print(True or False)   # true
print(False or False)  # false
print(not True)        # false
print(not False)       # true
```

**if-else 陳述句**

``` python
x=1
y=2
if x > y:
    x = x + y
else:  
    x = y - x

# 結果會走else 所以 x 等於 1
```

**迴圈**

迴圈有兩種for及while  

``` python
# for
no = [1,2,3,4,5,6,7,8,9]
x = 0
for i in no:  
    x = x + i
    
# for迴圈總共跑了9次
# x = 0 + 1
# x = 1 + 2
#    ...
# x = 28 + 8
# x = 36 + 9
# 結果 x 會等於 45 

# ---------------------------------------------
# while
x=0  
while x < 5:  
    x = x + 1

# while會跑5次 0<5 1<5 2<5 3<5 4<5 
# 結果 x 等於 5
```


## 免費佈署APP網站 Heroku
1. [註冊Heroku帳號](https://signup.heroku.com/login)  
First name：名字  
Last name：姓氏  
Email Address：信箱  
Role：職業  
Primary Development Language：主要開發語言  

2. 登入後新增新App ,點選 New -> Create New App
![](https://github.com/adgj5472/Python-Note/blob/master/img/heroku1.jpg)
