dict_nums = dict(x=list(range(11, 20))) 
dict1=dict(y=list(range(21, 30))) 
dict2=dict(z=list(range(31, 40)))
print(dict_nums)
print(dict1)
print(dict2)
print(dict_nums["x"][4])
print(dict1["y"][4])
print(dict2["z"][4])
for k,v in dict_nums.items():
    for a,b in dict1.items():
        for c,d in dict2.items():
            print(k, "has value", v)
    print(a,"has value",b)
print(c,"has value",d)
