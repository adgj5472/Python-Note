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

