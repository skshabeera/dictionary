a=[1,2,3,4,5,6]
b=["one","two","three","four","five"]
b.append(n)
i=0
d={}
while i<len(a):
    d[a[i]]=b[i]
    i=i+1
print(d)
    
# another method
# a=[1,2,3,4,5,6]
# b=["one","two","three","four","five"]
# c="six"
# b.append(c)
# d=zip(a,b)
# print(dict(d))
    
