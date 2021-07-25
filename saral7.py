dict={"frist":"1","second":"2","third": "1","four": "5","five":"5", "six":"9","seven":"7"}
list=[]
count=0
for i in dict.values():
    if i not in list:
        list.append(i)
        if count==1:
            list.append(i)
print(list)
# another method
a= [
    {"first":"1"}, 
    {"second": "2"}, 
    {"third": "1"}, 
    {"four": "5"}, 
    {"five":"5"}, 
    {"six":"9"},
    {"seven":"7"}
] 
b=[]
for i in a:
    for j in i.values():
        if j not in b:
            b.append(j)
print(b)
