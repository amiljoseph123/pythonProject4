d={1:4,0:2,3:4,2:1}
print(d)
sorted_d=sorted(d.items())
print("Ascending order:",sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print("descending order:",sorted_d)