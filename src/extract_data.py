import json 
import pandas as pd
import re

def extract_sections(text):
    sections = re.findall('^PHẦN THỨ.*', text)
    
    return sections

def extract_chapters(text):
    chapters = re.findall('^Chương.*', text)
    
    return chapters

def extract_items(text):
    items = re.findall('^Mục.*', text)
    
    return items

def extract_rules(text):
    rules = re.findall('^Điều.*', text)
    
    return rules 

def extract_clauses(text):
    clauses = re.findall('^\d.*', text)
    
    return clauses 

def extract_sub_clauses(text):
    sub_clauses = re.findall('^[a-z]\).*', text)
    
    return sub_clauses 

PATH = 'B:\\TT\\Project - information extraction\\data\\general\\rule_2015_clean.txt'
PATH_CLEAN_RULE = 'B:\\TT\\Project - information extraction\\data\\general\\rule_2015_clean_test.txt'

'''
clean_text = []

with open(PATH_CLEAN_RULE, 'r', encoding='utf-8') as file:
    for line in file:
        clean_text.append(line)
'''

PATH = 'B:\\TT\\Project - information extraction\\data\\general\\rule_2015_clean.txt'
with open(PATH_CLEAN_RULE, 'r', encoding='utf-8') as file:
    clean_text = file.read()

sections = []       # Các phần
chapters = []       # Các chương
items = []          # Các mục
rules = []          # Các điều
clauses = []        # Các khoản
sub_clauses = []    # Các khoản con

#print(clean_text)
#print(len(clean_text))

df = pd.DataFrame({
    'section': sections,
    'chapter': chapters,
    'item': items,
    'rule': rules,
    'sub_rule': clauses,
    'sub_sub_rule': sub_clauses
})

#print(df)

'''
for txt in clean_text: 
    tmp_section = extract_sections(txt)
    if tmp_section != []:
        sections.append(tmp_section)
        
    tmp_chapter = extract_chapters(txt)
    if tmp_chapter != []:
        chapters.append(tmp_chapter)
    
    tmp_item = extract_items(txt)
    if tmp_item != []:
        items.append(tmp_item)
    
    tmp_rule = extract_rules(txt)
    if tmp_rule != []:
        rules.append(tmp_rule)
        
    tmp_clause = extract_clauses(txt)
    if tmp_clause != []:
        clauses.append(tmp_clause)
        
    tmp_sub_clause = extract_sub_clauses(txt)
    if tmp_sub_clause != []:
        sub_clauses.append(tmp_sub_clause)
'''


#print(sections)
#print(len(sections))

PATH_SECTION = 'B:\\TT\\Project - information extraction\\data\\general\\section.txt'
PATH_CHAPTER = 'B:\\TT\\Project - information extraction\\data\\general\\chapter.txt'
PATH_ITEM = 'B:\\TT\\Project - information extraction\\data\\general\\item.txt'
PATH_RULE = 'B:\\TT\\Project - information extraction\\data\\general\\rule.txt'
PATH_CLAUSE = 'B:\\TT\\Project - information extraction\\data\\general\\clause.txt'
PATH_SUB_CLAUSE = 'B:\\TT\\Project - information extraction\\data\\general\\sub_clause.txt'

'''
with open(PATH_SECTION, 'w', encoding='utf-8') as file:
    for elem in sections:
        file.write(str(elem) + '\n')
        
with open(PATH_CHAPTER, 'w', encoding='utf-8') as file:
    for elem in chapters:
        file.write(str(elem) + '\n')
        
with open(PATH_ITEM, 'w', encoding='utf-8') as file:
    for elem in items:
        file.write(str(elem) + '\n')
        
with open(PATH_RULE, 'w', encoding='utf-8') as file:
    for elem in rules:
        file.write(str(elem) + '\n')
        
with open(PATH_CLAUSE, 'w', encoding='utf-8') as file:
    for elem in clauses:
        file.write(str(elem) + '\n')
        
with open(PATH_SUB_CLAUSE, 'w', encoding='utf-8') as file:
    for elem in sub_clauses:
        file.write(str(elem) + '\n')
'''

def extract_full_rules(text):
    rules = re.findall('^Điều.*', text)
    
    return rules 

def split_rules(text):
    all_rules = re.split(r'\. ', text)
    return all_rules
    
all_rules = split_rules(clean_text)
#print(all_rules)
#print(len(all_rules))

PATH_ALL_RULES = 'B:\\TT\\Project - information extraction\\data\\component\\full_rules.txt'

with open(PATH_ALL_RULES, 'w', encoding='utf-8') as file:
    for _ in range(len(all_rules)):
        file.write(all_rules[_] + '\n')