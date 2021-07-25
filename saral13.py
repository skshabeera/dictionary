dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':200}
max1=0
max2=0
max3=0
empty=[]
for i in dict:
     for j in dict:
        if dict[j]>max1:
            max1=dict[j]
            max1_key=j
        elif max1>dict[j] and max2<dict[j]:
            max2=dict[j]
            max2_key=j
        elif max2>dict[j] and max3<dict[j]:
            max3=dict[j]
            max3_key=j
empty.append(max1_key)
empty.append(max2_key)
empty.append(max3_key)
print(empty)