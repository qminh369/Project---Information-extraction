import json
import re
import pandas as pd

PATH_GEN_RET_DATA = 'B:\\TT\\Project - information extraction\\data\query\\small_query.txt'

data = []
with open(PATH_GEN_RET_DATA, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line)
        
clean_data = []
titles = []
querys = []

for ele in data:
    ele = re.sub('\n', '', ele)
    ele = re.sub('^Truy vấn: ', '', ele)
    ele = re.sub('^Truy vấn \d{1,2}: ', '', ele)

    if ele != '':
        clean_data.append(ele)
        
for idx in range(len(clean_data)):
    if idx % 2 == 0:
        titles.append(clean_data[idx])
    else:
        querys.append(clean_data[idx])
        
df = pd.DataFrame({
    'title': [],
    'query': []
})

for idx in range(len(titles)):
    print(idx)
    new_row = {'title': titles[idx], 'query': querys[idx]}
    df = df.append(new_row, ignore_index=True)
    
df = df.reset_index(drop=True)
print(df)

df.to_csv('B:\\TT\\Project - information extraction\\data\\query\\small_query.csv')
