import json
import re
import pandas as pd

#PATH_GEN_QA_DATA = 'B:\\TT\\Project - information extraction\\data\\general\\question_answer.txt'
#PATH_GEN_QA_DATA = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\question_answer.txt'
PATH_GEN_QA_DATA = 'B:\TT\Project - information extraction\data\data1006_QA\question_answer_val.txt'

data = []
with open(PATH_GEN_QA_DATA, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line)
        
clean_data = []
rules = []
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
    if idx % 3 == 0:
        rules.append(clean_data[idx])
    elif idx % 3 == 1:
        questions.append(clean_data[idx])
    else:
        answers.append(clean_data[idx])
       
#PATH_TEXT_FILE = 'B:\\TT\\Project - information extraction\\data\\data1008_QA\\data.txt' 
PATH_TEXT_FILE = 'B:\\TT\\Project - information extraction\\data\\data1008_QA\\data_val.txt' 

with open(PATH_TEXT_FILE, 'w', encoding='utf-8') as file:
    for i in range(len(questions)):
        file.write(questions[i] + '<|beginofdes|>' + answers[i] + '<|endofdes|>' + '\n' + 'xxxxxEndxxxxx' + '\n')
        


