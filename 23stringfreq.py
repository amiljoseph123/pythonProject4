str1=(input("enter the string"))
dict={}
for n in str1:
    if n in dict:
        dict[n]+=1
        print(dict)
    else:
        dict[n]=1
        print(dict)
print("character frequency")
for a,b in dict.items():
    print(a,b)