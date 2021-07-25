list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
new=[]
i=0
for i in  list1:
    if i%2!=0:
        new.append(i)
for i in list2:
    if i%2==0:
        new.append(i)
print(new)
