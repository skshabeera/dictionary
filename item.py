dic={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max1=0
max2=0
max3=0
for i in dic:
    for j in dic:
        if dic[j]>max1:
            max1=dic[j]
            max1_key=j
        elif max1>dic[j] and max2<dic[j]:
            max2=dic[j]
            max2_key=j
        elif max2>dic[j] and max3<dic[j]:
            max3=dic[j]
            max3_key=j
print(max1_key,max1)
print(max2_key,max2)
print(max3_key,max3)
