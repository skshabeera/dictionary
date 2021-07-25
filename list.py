l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
#o/p:{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
key=[]
for i in l:
    if i[0] not in key:
        key.append(i[0])
for k in key:
    b=[]
    for j in l:
        if j[0]==k:
            b.append(j[1])
    d[k]=b
print(d)
