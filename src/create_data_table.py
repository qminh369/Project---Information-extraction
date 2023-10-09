import pandas as pd

PATH_CONTEXT = 'B:\\TT\\Project - information extraction\\data\\component\\context.txt'
context = []
with open(PATH_CONTEXT, 'r', encoding='utf-8') as file:
    for line in file:
        context.append(line)
        
#print(len(context))

idx_rules = [i for i in range(1, len(context)+1)]
#print(idx_rules)

df = pd.DataFrame({
    'Rule': [],
    'Context': []
})

for idx in range(len(context)):
    new_row = {'Rule': idx_rules[idx], 'Context': context[idx]}
    df = df.append(new_row, ignore_index=True)
    #print(idx)

df.to_csv('B:\\TT\Project - information extraction\\data\\data_table.csv', index=False)