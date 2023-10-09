from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium import webdriver
import json
from random import randrange
import random
import pandas as pd
import time

# Thư viện undetected_chromedriver để vượt captcha
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
driver = uc.Chrome(chrome_options=chrome_options)

# Mở trang web ChatGPT
driver.get('https://chat.openai.com/auth/login')
time.sleep(3)

# Đăng nhập tài khoản chatgpt
button_login = driver.find_element(By.XPATH, "//div[@class='relative -top-[1px]']")
button_login.click()
time.sleep(3)

accounts = ['quangminhpulisic123@gmail.com', 'niallerjamespotter@gmail.com', 'phanan1227@gmail.com', 'tungteng0401@gmail.com', 'sktblank2212@gmail.com']
passwords = ['minhboy123', '12345678', 'phanlacan12', '@jTtM*wUvT4B62.', 'minhkepa2212']

idx_rand = randrange(0, len(accounts))

# Nhập tài khoản, mật khẩu
mail = driver.find_elements(By.TAG_NAME, "input")[1]
mail.send_keys(accounts[idx_rand])
time.sleep(3)
btn = driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

pw = driver.find_elements(By.TAG_NAME,"input")[2]
pw.send_keys(passwords[idx_rand])
time.sleep(3)
# Button continue
btn = driver.find_element(By.XPATH, "//button[@class = 'ce7494284 c24f2ad5c c5bf19ed3 c66fbaaf0 _button-login-password']")
btn.click()
#btn = driver.find_elements(By.TAG_NAME,"button")[0]
#btn.click()
time.sleep(15)

#time.sleep(30)
# Button not usually 
#btn1 = driver.find_elements(By.TAG_NAME, "button")[0]
#btn1 = driver.find_element(By.XPATH, "//div[@class = 'flex w-full gap-2 items-center justify-center']")
btn1 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-primary']")
btn1.click()

PATH_GENERAL_PROMPT_CHATGPT = 'B:\\TT\\Project - information extraction\\data\\general\\general_prompt_chatgpt.txt'
PATH_GENERAL_PROMPT_VIETNAMESE = 'B:\\TT\\Project - information extraction\\data\\general\\general_prompt_vietnamese.txt'
PATH_GENERAL_PROMPT_QA = 'B:\\TT\\Project - information extraction\\data\\general\\general_prompt_qa.txt'

with open(PATH_GENERAL_PROMPT_QA, 'r', encoding='utf-8') as file:
    general_prompt = file.read()

#number_of_examples = 100
#number_of_examples = 50
#number_of_examples = 20
#number_of_examples = 10
#number_of_examples = 5      # Gen valid dataset
#number_of_examples = 3
number_of_examples = 5

#questions = []

PATH_ALL_RULES = 'B:\\TT\\Project - information extraction\\data\\component\\full_rules.txt'

rules = []
with open(PATH_ALL_RULES, 'r', encoding='utf-8') as file:
    for line in file:
        rules.append(line)
#print(len(rules))

#PATH_QUESTION_ANSWER = 'B:\\TT\\Project - information extraction\\data\\general\\question_answer.txt'
PATH_QUESTION_ANSWER = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\question_answer.txt'
#PATH_QUESTION_ANSWER = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\question_answer_val.txt'

for i in range(number_of_examples):
    i_rand = randrange(0, len(rules))
    # Correct
    # prompt = f'A model that takes in a long request with description to perform only "{questions[i_rand]}" task, tasks require rules answer. Give response in format "Rule:..."'
    prompt = f'Một mô hình có khả năng đưa ra câu trả lời với mô tả duy nhất như sau "{rules[i_rand]}". Đưa ra câu trả lời với định dạng: Điều:...\nCâu hỏi:...\nCâu trả lời:...'
    # Interact chatgpt
    text_area = driver.find_element(By.TAG_NAME, "textarea")
    driver.execute_script("arguments[0].value = arguments[1];", text_area, general_prompt + prompt)
    text_area.send_keys(Keys.ENTER)

    btn_answer = driver.find_element(By.XPATH, "//button[@class = 'absolute p-1 rounded-md md:bottom-3 gizmo:md:bottom-2.5 md:p-2 md:right-3 dark:hover:bg-gray-900 dark:disabled:hover:bg-transparent right-2 disabled:text-gray-400 enabled:bg-brand-purple gizmo:enabled:bg-transparent text-white gizmo:text-gray-500 gizmo:dark:text-gray-300 bottom-1.5 transition-colors disabled:opacity-40']")
    btn_answer.click()
    #time.sleep(40)
    #time.sleep(40)
    time.sleep(60)
    
    #answer = driver.find_elements(By.XPATH, "//div[@class = 'markdown prose w-full break-words dark:prose-invert light']")[i]
    answer = driver.find_elements(By.XPATH, "//div[@class = 'markdown prose w-full break-words dark:prose-invert dark']")[i]
    result = answer.text
    print(result)
    
    with open(PATH_QUESTION_ANSWER, 'a', encoding='utf-8') as file:
        file.write(result + '\n')
    
    print(i)

    #time.sleep(5)
    time.sleep(1)

driver.quit()
