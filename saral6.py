dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
dict={} 
for key,value in dic.items():
    if key not in dict.keys():
        dict[key]=value
print(dict)

    
