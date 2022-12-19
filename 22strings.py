n=int(input("enter the number of strings"))
print("strings are:")
list=[]
for i in range(0,n):
    n=str(input())
    list.append(n)
print(list)
count=0
for i in list:
    for j in i:
        if j =='a':
            count=count+1
print(count)


