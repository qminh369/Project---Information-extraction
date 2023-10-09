import json
import csv
import random

def shuffle_jsonl_file(input_file, output_file):
    # Load JSONL file and parse into a list of JSON objects
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    json_objects = [json.loads(line) for line in lines]
    
    # Shuffle the list of JSON objects
    random.shuffle(json_objects)
    
    # Write shuffled JSON objects back to a new JSONL file
    with open(output_file, 'w') as f:
        for json_obj in json_objects:
            f.write(json.dumps(json_obj) + '\n')
            
def shuffle_csv(input_file, output_file):
    # Đọc dữ liệu từ tệp CSV vào danh sách
    data = []
    with open(input_file, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Lấy tiêu đề nếu có
        for row in csv_reader:
            data.append(row)

    # Xáo trộn dữ liệu
    random.shuffle(data)

    # Ghi dữ liệu xáo trộn vào tệp CSV đầu ra
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        if header:
            csv_writer.writerow(header)  # Ghi lại tiêu đề nếu có
        csv_writer.writerows(data)

# Example usage
#input_file_jsonl = 'B:\\TT\\Project - information extraction\\data\\QA_chatbot\\rule_qa.jsonl'
#output_file_jsonl = 'B:\\TT\\Project - information extraction\\data\\QA_chatbot\\shuffle_rule_qa.jsonl'
#shuffle_jsonl_file(input_file_jsonl, output_file_jsonl)

#input_file_csv = 'B:\\TT\\Project - information extraction\\data\\QA_chatbot\\rule_qa.csv'
#output_file_csv = 'B:\\TT\\Project - information extraction\\data\\QA_chatbot\\shuffle_rule_qa.csv'

#input_file_csv = 'B:\\TT\\Project - information extraction\\data\\query\\small_query.csv'
#output_file_csv = 'B:\\TT\\Project - information extraction\\data\\query\\shuffle_small_query.csv'

#input_file_csv = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\rule_qa.csv'
#output_file_csv = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\shuffle_rule_qa.csv'

input_file_csv = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\rule_qa_val.csv'
output_file_csv = 'B:\\TT\\Project - information extraction\\data\\data1006_QA\\shuffle_rule_qa_val.csv'
shuffle_csv(input_file_csv, output_file_csv)