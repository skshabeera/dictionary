str="my name is shabeera"
dict={}
for i in range(len(str)):
    if str[i]=="is":
        dict["is"]=i
    i=i+1
print(dict)
            