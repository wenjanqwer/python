# 集合運算
#s1={3,4,5}
#s2={4,5,6,7}
#print(3 in s1)
#print(10 not in s1)
#s3=s1&s2 #交集: 取倆的集合中相同資料
#s4=s1|s2 #聯集: 取兩個集合中所有資料，不重複取
#s3=s1-s2 #差及: 從s1中減去和s2相同部分
#s3=s1^s2 #反交集: 取兩個集合中部重疊部分
#print(s3)
#s=set("hello") #set(字串) 字串拆成集合
#print(s)
#print("h" in s)
# 字典運算 key-value 配對
#dic={"apple":"蘋果","bug":"蟲蟲"}
#dic["apple"]="小蘋果"
#print(dic["apple"])
#print("apple" in dic) #判斷 key 是否存在 
#print("test" not in dic)
#print(dic)
#del dic["apple"] #刪除字典中的健值對 (key-value pair)
#print(dic)
# 列表建立字典
dic={x:x*2 for x in [3,4,5]} #列表建立字典 語法是這樣 in 後面要列表
print(dic)