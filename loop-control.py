# break 的簡易範例

# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) #印出迴圈中的n
#     n+=1

# print("最後的n: ",n) #印出迴圈結束後的n

# continue 的簡易用法
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # x 是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的n: ",n)

# else 簡易範例

# sum=0
# for x in range(1,11):
#     sum+=x
# else:
#     print(sum) #上面迴圈跑完才做else，迴圈結束前執行這命令，印出0+1+2+.....+10=55的結果

#綜合範例:找出整數平方根
#輸入 9 ，得到 3
#輸入 11， 得到【沒有】整數平方根

n=input()
n=int(n)
for i in range(n): #0到n-1
    if i*i==n:
        print("整數平方根",i)
        break #用break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根")
