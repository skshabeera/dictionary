word="MISSISSIPPI"
a={}
for c in word:
    if c not in a:
        a[c]=1
    else:
        a[c]=a[c]+1
print(a)
# another method
str1 = "Apple"
Dict = {}
for char in str1:
  count = str1.count(char)
  Dict[char]=count
print(Dict)