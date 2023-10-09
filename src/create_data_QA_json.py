import json
import re
import pandas as pd

PATH_GEN_QA_DATA = 'B:\\TT\\Project - information extraction\\data\\general\\question_answer.txt'

data = []
with open(PATH_GEN_QA_DATA, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line)
        
clean_data = []
questions = []
answers = []

for ele in data:
    ele = re.sub('\n', '', ele)
    ele = re.sub('^Để tạo ra.*', '', ele)
    ele = re.sub('^Để sinh.*', '', ele)
    ele = re.sub('^Dưới đây.*', '', ele)
    ele = re.sub('^Để chuẩn bị dữ liệu.*', '', ele)
    ele = re.sub('^\d{1,2}. ', '', ele)
    ele = re.sub('Câu hỏi: ', '', ele)
    ele = re.sub('Câu trả lời: ', '', ele) 
    ele = re.sub('^Câu hỏi \d{1,2}: ', '', ele)
    ele = re.sub('^Câu trả lời \d{1,2}: ', '', ele)
    ele = re.sub('^Câu Hỏi \d{1,2}:', '', ele)
    ele = re.sub('^Câu Trả Lời \d{1,2}:', '', ele)
    if ele != '':
        clean_data.append(ele)
        
for idx in range(len(clean_data)):
    if idx % 2 == 0:
        questions.append(clean_data[idx])
    else:
        answers.append(clean_data[idx])
        
df = pd.DataFrame({
    'question': [],
    'answer': []
})

for idx in range(len(answers)):
    print(idx)
    new_row = {'question': questions[idx], 'answer': answers[idx]}
    df = df.append(new_row, ignore_index=True)
    
df = df.reset_index(drop=True)
print(df)

df.to_csv('B:\\TT\\Project - information extraction\data\\QA_chatbot\\rule_qa.csv')
df.to_json('B:\\TT\\Project - information extraction\data\\QA_chatbot\\rule_qa.jsonl', orient='records', lines=True)
df.to_json('B:\\TT\\Project - information extraction\data\\QA_chatbot\\rule_qa.json')