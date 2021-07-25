n=int(input('enter the number'))
i=1
a=[]
dic={}
while i<=n:
	j=1
	b=[]
	a.append(i)
	while j<=10:
		d=i*j
		b.append(d)
		j=j+1
	dic[i]=b
	i+=1
print(dic)