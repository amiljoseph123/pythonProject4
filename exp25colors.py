list1=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    i = input()
    list1.append(i)
print(list1)
list2=[]
z = int(input("Enter number of elements : "))
for i in range(0, z):
    i = input()
    list2.append(i)
print(list2)
print("colours present only in list 1 :")
x=list(set(list1).difference(list2))
print(x)