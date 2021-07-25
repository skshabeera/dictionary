list=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

for i in range(len(list)):
    if list[i]['id'] =='#FF0000':
        del list[i]
        break
print("after",list)