a=input("enter the text")
dict1={}
b=a.split()
for i in b:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i]=1
print("word frequency")
for x,y in dict1.items():
    print(x,y)


