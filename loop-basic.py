# while 迴圈
# 1+2+3+...+10
#n=1
#sum=0 #紀錄累加結果
#while n<=10:
#    sum+=n
#    n+=1
#print(sum)
# for 迴圈
#for x in [3,5,1]:
#    print(x)
#for q in "hello":
#    print(q)
#for x in range(5):
#    print(x)
#for x in range(5,10): #range(5,10) 包含開頭不包含結束
#    print(x)
#range用法 range(start,end,step)
#sum=0
#for x in range(1,11):
#    sum+=x
#print(sum)


# 班導ppt範例3
"""
a="*"
b=-1

for s in range(0,7):
    if s<4 :
        b=b+2
        c=a*b
        print(c)
    elif s>=4:
        b=b-2
        c=a*b
        print(c)    
"""


# 班導ppt範例4
a=input()
y=[]
sum=0

for s in range(3):
    b=a*(3)+a*(s*2)
    x=int(b)
    y=y+[x]
print("\n",y)

for d in y:
    sum+=d
print("\n",sum)