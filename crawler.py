import csv
import requests
from bs4 import BeautifulSoup
import json
import string

fields = list()
rows = list()

def get_all_links(alphabet):
    filename = f'./my_files/csv_files/{alphabet}.csv'
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        # Extracting field names through first row
        fields = next(reader)
        # Extracting data from each row one by one
        for row in reader:
            rows.append(row)
        # print("Total no. of rows: %d"%(reader.line_num))
    return rows


for alphabet in string.ascii_lowercase[14]:
    word_links = get_all_links(alphabet)
    total_list = list()

    for url in [word_links[i] for i in range(len(word_links))]:
        # print(url[1])
        response = requests.get(url[1])

        if response.status_code == 200:
            bs_obj = BeautifulSoup(response.text, 'html.parser')
            if bs_obj.find('span', {'class': 'pron-spell-content'}):
                pronunciation = bs_obj.find('span', {'class': 'pron-spell-content'}).get_text()
            all_meanings = bs_obj.find('div', {'class': 'e16867sm0'}).findAll('section', {'class': 'css-pnw38j'})
            current_word = dict()

            all_meanings_dict = dict()
            for meaning in all_meanings:
                grammar = ''
                lines= ''

                if meaning.find('span', {'class': 'luna-pos'}) or meaning.find('span', {'class': 'pos'}):
                    if meaning.find('span', {'class': 'luna-pos'}):
                        grammar = meaning.find('span', {'class': 'luna-pos'}).get_text()
                    elif meaning.find('span', {'class': 'pos'}):
                        grammar = meaning.find('span', {'class': 'pos'}).get_text()
                    lines = meaning.findAll('div', {'class': 'e1q3nk1v2'})
                    grammarwise_meaning = dict()
                    each_grammar_meaning = dict()
                    i = 1
                
                    for line in lines:
                        subject = ''
                        example = ''
                        each_meaning = dict()

                        if line.find('span', {'class': 'italic'}):
                            subject = line.find('span', {'class': 'italic'}).get_text()
                        text = line.findAll('span')[-1].get_text()
                        if line.find('span', {'class': 'luna-example'}):
                            example = line.find('span', {'class': 'luna-example'}).get_text()
                        each_meaning['subject'] = subject
                        each_meaning['text'] = text
                        each_meaning['example'] = example
                        each_grammar_meaning[i] = each_meaning
                        i += 1

                    all_meanings_dict[grammar] = each_grammar_meaning
                        
            current_word['word'] = url[0]
            current_word['pronunciation'] = pronunciation
            current_word['meaning'] = all_meanings_dict

        total_list.append(current_word)


        with open(f'./my_files/json_files/{alphabet}.json', 'w', encoding='utf-8') as file:
            json.dump(total_list, file, ensure_ascii=False, indent=4)