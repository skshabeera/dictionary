a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
c={}
for d in a:
    if d['item'] not in c:
        c[d['item']] = d['amount']
    else:
        c[d['item']] += d['amount']  
print(c) 