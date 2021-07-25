a=['s001','s002','s003','s004']
b=['adina park','Leyton Marsh','Duncan Boyle','saim Richards']
c=[85,98,89,92]
dic={}
list=[]
i=0
while i<len(a):
    dic1={}
    dic1[b[i]]=c[i]
    dic[a[i]]=dic1
    i+=1
list.append(dic)
print(list)
