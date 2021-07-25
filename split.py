a={'s 001':['maths','science'],'s 002':['maths','english']}
d={}
for x,y in a.items():
    b=x.split()
    c=b[0]+b[1]
    d.update({c:y})
print(d)
# another method
dic={'s 001':['maths','science'],'s 002':['maths','english']}
dict={}
for key,value in dict.items():
    c=key.split()
    i=0
    while i<len(c)-1:
        d=c[i]+c[i+1]
        i=i+1
        dict[d]=value
print(dict)