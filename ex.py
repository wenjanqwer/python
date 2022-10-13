#班導的題目
print("題目 : Jumping Mario")
x=int(input("輸入測資數量:"))
q=[]
w=[]
for i in range(x):
    print("------測資%d------"%(i+1))
    y=int(input("輸入牆壁數量:"))
    w=w+[y]
    for j in range(y):
        z=int(input("牆壁%d:"%j))
        q=q+[z]
h=0
l=0
r=0
for i in range(x):
    e=w[i]-1
    for j in range(e):
        if q[r]<q[r+1]:
            h=h+1
        elif q[r]>q[r+1]:
            l=l+1
        r=r+1
    print("Case %d"%(i),":  high jumps= %d"%(h),",  low jumps= %d "%(l))
    h=0
    l=0
    r=r+1    
    

