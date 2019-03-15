# Python-Note

## ToDo
  
* line API 介紹  



## 安裝
基本上一直下一步就好了  
[python3.7.2](https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe)  

## Python 語法基礎
變數(variables)與資料型態、型別(types)  
* 賦予名字給某個值  
* 在程式裡重複使用  
* 值可以不斷被改變  

### 變數名稱保留字(不能拿來當變數名稱):

| and | as | assert | break | class |
| :------| ------: | :------: | :------: | :------: |
| continue | def | del | elif | else |
| except | finally | for | from | global |
| if | import | in | is | lambda |
| not | or | pass | print | raise |
| return | try | while | with | yield |

### 指定變數的語法：

``` python
x = 20  # 代表x等於20,等於不是數學內相等的意思,而是指定,左右不能互換
```

### 使用變數：
``` python
x = 10
y = x * 40    # 結果 y 等於400
```

### 基本運算

| 二元運算子 | 用法 | 說明 |
| :------| ------: | :------: |
| + | X + Y | X加上Y |
| - | X - Y | X減去Y |
| * | X * Y | X乘以Y |
| / | X / Y | X除以Y |
| % | X % Y | 取X除以Y的餘數 | 

``` python
print(5 + 3)    # 8
print(25 - 10)  # 15
print(5 * 3)    # 15
print(10 / 5)   # 2
print(21 % 2)   # 1     21/2 的餘數為 1，所以結果為 1  
print(3 ** 5)   # 243   3 的 5 次方  
```

### 比較運算子

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

### 邏輯運算子

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

### if-else 陳述句

``` python
x=1
y=2
if x > y:
    x = x + y
else:  
    x = y - x

# 結果會走else 所以 x 等於 1
```

### 迴圈

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

### list
* 當資料如果有一整串時，在 Python 裡，list 可以表示這種類型的資料  
* 用一對中括弧 [] 來代表一個 list 的開始與結束，list 中的元素用逗號分隔  

``` python
a = ['red', 'blue', 'orange', 'black']  
len(a)   #可以用 len 函式來檢視它的長度  
a[0]     #取得 list 中第一個元素的元素  
a[-1]    #從後面取得 list 中的元素  

# 結果
# 4
# red
# black
#
# 解說:
# 1. a 是我們想檢視的 list
# 2. index 是從 0 開始而非 1 
# 3. 因此 'red' 在這個 list 中的位置是 0 而非 1

```

取得 list 中的「其中一部分」  

``` python
a = ["1", "2", "3", "4", "5", "6", "7"]  
print(a[3:6])  # ['4', '5', '6', '7'] 
print(1[:5])   # ['1', '2', '3', '4']

# 結果
# ['4', '5', '6', '7'] 
# ['1', '2', '3', '4']

# 解說:
# 1.中括弧裡面的內容包含一個冒號：
# 2.冒號前是開始位置 
# 3.冒號後是結束位置
# 4.結果並不包含結束項
```

改變 list 中的內容：  

``` python
a = ["1", "2", "3", "4", "5", "6", "7"]  
a[0] = 'first'  
print(a)  

# 結果:
# ['first', '2', '3', '4', '5', '6', '7']
```

增加 list 的內容 可以使用 append 方法：  

``` python
a = ["1", "2", "3", "4", "5", "6", "7"]  
a.append('eight')  
print(a)  

# 結果:
# ['1', '2', '3', '4', '5', '6', '7', 'eight']
```

### dict(字典)
* 用一對大括弧 {} 來表示一個 dict 的開始與結束
* 每一個元素都是一組 key-value
* key 即是索引，每個索引對到一個值 
* key 與 value 中間用冒號隔開，每組之間用逗號隔開
* 使用方法很類似 list，但 dict 是以 key 代表值的位置

查看內容  
``` python
a = {'name': 'Ben', 'height': 178}  
print(a['height']) 

# 結果:
# 178
```

增加資料到字典中  
``` python
a = {'name': 'Ben', 'height': 178}  
a['age'] = 18  
print(a)

# 結果:
# {'name': 'Ben', 'height': 178, 'age': 18}  
```

更新字典內的元素  
``` python
a = {'name': 'Ben', 'height': 178}  
a.update({'height': 200})  
print(a)

# 結果:
{'name': 'Ben', 'height': 200}
```

將 dict 裡的資料全部讀出來  
``` python
# 遍歷整個字典資料
a = {'name': 'Ben', 'height': 200}
for rec in a:  
    print("key:"+rec+" value:"+a[rec])
    
# 結果:
# key:name value:Ben 
# key:height value:200 
```
    
### 函式(function)
將重複使用的程式碼轉換為一個函式，有效簡化程式碼，並可重複利用，也可將函式當成一個函式的輸入(lambda)  

先前有使用過的函式：
``` python
# print: 印出某個值
# len: 取得一個串列的長度

a = len(list)  
print(a)

# 結果:
# 5

# 解釋
# 1. len 是函式名稱
# 2. 函式名稱之後須加一對括弧，括弧間的是函式的輸入
# 3. 在這裡只有一個輸入，即 list
# 4. 若有多個輸入值，則用逗號分隔( , )
# 5. 5 是print這個函數呼叫的輸出
```
函式撰寫方式 
``` python 
def 函式名稱(參數1,參數2,參數3,.....):
    # 以縮排來判斷同一個函式區塊
```    
``` python 
# 函式
def addNum(a, b): # 函式命名標準會採取駝峰式的樣式  
    return a+b
    
print(addNum(1,4))

# 結果
# 5
```

如果要在函式的輸入值不預先定義有幾個，可以透過下列語法：  
``` python 
# 接受多個 Key/Value 參數
def make_two_lists(**kwargs):  
    keys,values = [],[]
    for k,v in kwargs.items():
        keys.append(k)
        values.append(v) 
    return [keys,values]

make_two_lists(david='M', Mary = 'F', John='M')  

# 結果
[['John', 'Mary', 'david'], ['M', 'F', 'M']]
```

### 函式庫(libraries)
* 前人寫好的一堆函式
* 使用者可以「引用」(import) 函式庫來使用這些函式
* 讓程式碼更簡潔且開發更快速

``` python
# 引用函式庫，並顯示目前的時間
import time

# 我們可以使用這個函式庫裡面的函式strftime
proc_time = time.strftime("%Y-%m-%d %H:%M:%S")  
print(proc_time)  

# 結果:
# 2017-09-21 06:51:11

# 也可以只引用函式庫中的其中某幾個函式 

# from 後面接的是函式庫名稱，import 後接的是函式名稱
from random import choice  
choice([1, 5, 7, 3, 9, 0])

# 結果
# 5
```

### 檔案(file)
主要描述該如何讀取檔案內容以及對檔案的操作  
``` python
# 寫檔
#將Hello World 寫入檔案中 
fid = open('test.txt', 'w')  
fid.write('Hello\nWorld')  
fid.close()  


# 讀檔
# 一行一行讀取檔案
with open('test.txt', 'r') as fid:  
    for line in fid:
        print("Line: " + line.strip())

# 結果
# Line: Hello 
# Line: World 


# 讀取檔案中所有內容
with open('test.txt', 'r') as fid:  
    s = fid.read() 
    print("讀取檔案中所有內容line =>"+s)
    
# 讀取檔案中所有內容line => Hello World
```

### 錯誤偵測(try catch)
程式在執行的過程中，往往會遇到錯誤狀況，例如：型別錯誤，資料讀取錯誤等  
為了避免一發生錯誤程式就停止且能夠即時紀錄或顯示錯誤資訊，就必須做好錯誤判斷的處理  

``` python
# 處理 IO Exception
try:  
    f = open('testfile','w') 
    f.write('Test write this')
except IOError: # 發生IOError類的錯誤 處理IOError  
    print("Error: Could not find file or read data")
else: # 發生其他錯誤
    print("Content written succesfully")
f.close()  
```

## 創建Line Bot  
1. 使用line帳號登入  

[進入Line 控制台](https://developers.line.me/console/)  

2. 創建提供者  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line0.jpg)  

3. 填入提供者名稱  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line1.jpg)  

4. 創建提供者  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line2.jpg)  

5. 新增一個channel  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line3.jpg)  

6. 填入資訊  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line4.jpg)  

7. 同意條款  
![](https://github.com/adgj5472/Python-Note/blob/master/img/line5.jpg)  
![](https://github.com/adgj5472/Python-Note/blob/master/img/line6.jpg)  

## 架設一的簡單的機器人  

1. (下載範例程式)[https://github.com/adgj5472/Heroku-Linebot-Sample/archive/master.zip]  
將檔案下載後解壓縮放置D槽  

2. [進入Line 控制台](https://developers.line.me/console/) 選擇創建的channel  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line7.jpg)  

3. 開啟 webhook

![](https://github.com/adgj5472/Python-Note/blob/master/img/line8.jpg)  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line9.jpg)  

4. 關閉預設罐頭回覆訊息  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line10.jpg)  

5. 產生 Channel access token  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line11.jpg)  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line12.jpg)  

6. 取得 Channel access token

![](https://github.com/adgj5472/Python-Note/blob/master/img/line13.jpg)  

7. 取得 Channel secret

![](https://github.com/adgj5472/Python-Note/blob/master/img/line14.jpg)  

8. 使用編輯器開啟範例程式碼資料夾內的 app.py,把剛剛取得的 channel secret 和 channel access token 填入

![](https://github.com/adgj5472/Python-Note/blob/master/img/line15.jpg)  


## 免費佈署APP網站 Heroku
### 註冊及新增 Heroku App
1. [註冊Heroku帳號](https://signup.heroku.com/login)  

![](https://github.com/adgj5472/Python-Note/blob/master/img/heroku0.jpg)  

First name：名字  
Last name：姓氏  
Email Address：信箱  
Role：職業  
Primary Development Language：主要開發語言  

2. 登入後新增新App ,點選 New -> Create New App  

![](https://github.com/adgj5472/Python-Note/blob/master/img/heroku1.jpg)  

3. 設定 App 名稱  

region 選擇 United States  

![](https://github.com/adgj5472/Python-Note/blob/master/img/heroku1.jpg)  

### 將程式推到 Heroku 上  
1. 下載並安裝  

* [Heroku CLI](https://cli-assets.heroku.com/heroku-x64.exe)  

* [Git](https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe)  

2. 開啟cmd  並移動到D槽  
搜尋cmd並開啟  
![](https://github.com/adgj5472/Python-Note/blob/master/img/heroku3.jpg)  

![](https://github.com/adgj5472/Python-Note/blob/master/img/cmd0.jpg)  

``` bash
$ D: 
$ cd Heroku-Linebot-Sample-master
```

3. 使用終端或命令行應用程序登錄到 Heroku  

``` bash
$ heroku login  
```

輸入完按下enter,開啟網頁,並輸入帳號密碼,完成後 cmd 顯示登入成功  

![](https://github.com/adgj5472/Python-Note/blob/master/img/cmd1.jpg)  

4. 初始化 git  

``` bash
$ git config --global user.name 你的名字  
$ git config --global user.email 你的信箱  
```

![](https://github.com/adgj5472/Python-Note/blob/master/img/cmd2.jpg)  

**注意：git init 僅第一次使用時要輸入**  

``` bash
$ git init
```

![](https://github.com/adgj5472/Python-Note/blob/master/img/cmd3.jpg)  

6. 用 git 將資料夾與 heroku 連接  

**注意：{HEROKU_APP_NAME} 是剛剛上面新增的 Heroku App名稱**  

``` bash
$ heroku git:remote -a {HEROKU_APP_NAME}
```

![](https://github.com/adgj5472/Python-Note/blob/master/img/cmd4.jpg)  

7. 輸入以下指令，將程式碼推上 Heroku，如果有跳出錯誤請重新輸入  

**每當需要更新 Bot 時，請重新輸入下面指令**  

``` bash
$ git add .
$ git commit -m "這邊填註解(簡單的說一下這次做了些什麼改動)"
$ git push -f heroku master
```

這樣代表成功推上去了  
![](https://github.com/adgj5472/Python-Note/blob/master/img/cmd5.jpg)  

## 將 Heroku 與 Line 綁定

1. [進入Line 控制台](https://developers.line.me/console/) 選擇創建的channel  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line7.jpg)  

2. 在 webhook URL 中輸入 Heroku 網址  
``` python
{HEROKU_APP_NAME}.herokuapp.com/callback

# 例如我的 APP NAME 是 python-linebot-test
# python-linebot-test.herokuapp.com/callback
```

![](https://github.com/adgj5472/Python-Note/blob/master/img/line16.jpg)  

![](https://github.com/adgj5472/Python-Note/blob/master/img/line17.jpg)  

3. 掃描你的LINE頁面QRCOD加入你的line機器人好友

![](https://github.com/adgj5472/Python-Note/blob/master/img/line18.jpg)  

4. 對你的機器人傳訊息,他就會給你簡單的回應囉

![](https://github.com/adgj5472/Python-Note/blob/master/img/line19.jpg)  

