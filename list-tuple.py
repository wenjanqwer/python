# 有順序可便動列表list
grades=[12,60,15,70,90]
#grades=grades+[12,30]
#grades[1:4]=[] # 把1到3的資料刪除
#print(grades)
#length=len(grades) #取得列表長度 len(列表資料)
#print(length)
#print(grades[1:4]) #取從編號1到4但不包含四，跟字串一樣
print(grades[1:4:2])
#grades[0]=55 # 把55放到列表中第一位址
#print(grades[0])
#data=[[1,2,3],[4,5,6]] #巢狀列表
#data[0][0:2]=[5,5,5]
#print(data)
# 有順序不可便動列表tuple 
data=(3,4,5)
#data[0]=5 #錯誤: tuple資料不可變動其他部分跟;ist一樣
print(data[0:2])