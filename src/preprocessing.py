import re 
import string

def strip_all_line(text: str):
    text = text.strip()
    return text

def remove_all_punctuation(text: str):
    translator = str.maketrans('', '', string.punctuation)
    text_no_punctuation = text.translate(translator)
    return text_no_punctuation    
    
def remove_newline(text: str):
    text = re.sub('\n', ' ', text)
    
    return text

def remove_punctuation(text: str):
    text = re.sub('[;:]', '', text)
    
    return text

def remove_first_number(text: str):
    text = re.sub('^\d. ', '', text)
    return text

def remove_not_rules(text: str):
    text = re.sub('^PHẦN.*', '', text)
    text = re.sub('^CHƯƠNG.*', '', text)
    text = re.sub('^MỤC.*', '', text)
    return text
        
def preprocessing(text: str):
    text = strip_all_line(text)
    #text = remove_all_punctuation(text)
    text = remove_punctuation(text)
    text = remove_first_number(text)
    text = remove_newline(text)
    
    return text

INPUT = 'B:\\TT\\Project - information extraction\\data\\general\\rule_2015.txt'
OUTPUT = 'B:\\TT\\Project - information extraction\\data\\general\\rule_2015_clean_test.txt'

with open(INPUT, 'r', encoding='utf-8') as file:
    text = file.read()
    
clean_text = preprocessing(text)
print(clean_text)

with open(OUTPUT, 'w', encoding='utf-8') as file:
    file.write(clean_text)
    