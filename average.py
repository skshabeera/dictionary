# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# for i in student_details:
#     n1=i.pop('V')
#     n2=i.pop('VI')
#     i['V+VI']=(n1+n2)/2
# print(student_details)
    
# list=[6,1,3,5,6,3,1]
# i=0
# mul=1
# c=0
# while i<len(list):
#     if list[i]  in list:
#           if c==1:
#                 mul=mul*list[i]
          
#           i=i+1
# print(mul)
        
list=[6,1,3,5,6,3,1]
i=0
mul=1
a=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        mul=mul*a[i]
    i=i+1
print(mul)