from bs4 import BeautifulSoup
import requests
import csv
import string

for alphabet in string.ascii_lowercase:
    all_words_list = list()
    
    for page_no in range(1, 100):
        url = f'https://www.dictionary.com/list/{alphabet}/{page_no}'
        response = requests.get(url)

        if response.status_code == 200:
            bs_obj = BeautifulSoup(response.text, 'html.parser')
            word_list = bs_obj.find('ul', {'class': 'e12ye68r0'}).findAll('li')

            # Unpacking both iterables in a list literal using *
            all_words_list = [*all_words_list, *list(word_list)]
        else:
            break


    with open(f'./my_files/csv_files/{alphabet}.csv', 'w', encoding='UTF8') as file:
        header = ['word', 'link']

        writer = csv.writer(file)
        writer.writerow(header)

        for llist in all_words_list:
            data = list()
            word = llist.a.get_text()
            link = llist.a.attrs['href']
            data = [word, link]

            writer.writerow(data)
