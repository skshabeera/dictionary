# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)

dict =  {
    'Alex': ['subj1', 'subj2', 'subj3'], 
    'David': ['subj1', 'subj2']}
total=0
for value in dict:
    value_list=dict[value]
    count=len(value_list)
    total=total+count
print(total)
# dict={"siri":20,"anusha":21,"shabeera":23}
# total=0
# for value in dict:
#     value_list=dict[value]
#     count=dict.len()
#     toatal=total+count
# print(total)