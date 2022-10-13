# 數字運算
"""
x=3*6
y=3/6 #小數除法
z=7//6 # 整數除法，不會4捨5入
a=2**0.5 # 次方
b=7%3 #取餘數
c=2+3
c+=1 #c=c+1 將變數中的數字加1
d=2+3
d-=1
e=2+3
e*=2
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
"""
# 字串運算
# 字串會對內部字源編號(索引)，從0開始算起　
s="holle" # 字串可以用2種方式建立，單引號跟雙引號都可以
print(s)
q="holl\"e" # \代表跳脫
w= "holle"+"word" # 字串串接可以用+或空白
s="holle\nword" #表達多行的字\n
m="""holle 

word""" # 也是換行一定要3個單引號或雙引號
f="holle"*3+"word" #重複3次+word
print(f)
print(s[1:4]) #包含開頭不包含結尾 語法:變數名稱[start:end:step]

