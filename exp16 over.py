n=int(input("enter the number of elements"))
list=[]
print("the elements are:")
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        list.append("over")
    else:
        list.append(ele)
print(list)