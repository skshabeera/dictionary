n={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# o/p=[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
b=[]
for i in n.values():
    b.append(i)
b1=[]
i=0
while i<4:
    j=0
    d={}
    for k in n:
        d[k]=b[j][i]
        j=j+1
    b1.append(d)
    i=i+1
print(b1)
