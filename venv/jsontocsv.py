#

import json
import csv

#данная функция открывает json файл по территории, убирает первый общий уровень data и отдает json файл в формате списка словарей
def getJson (path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f) #data в формате dict

        cards = data['data'] #cards в формате str, избавились от первого общего ключа data
        data_clear = json.loads(cards) #формат dict без первого общего ключа data
        cards_dict = data_clear['cards']
      #  data_dict = json.loads(cards)
        return cards_dict


    #записали в файл рабочий список
    #with open('cards_dict.json', 'w', encoding='utf-8') as write_file:
    #    json.dump(cards_dict, write_file, ensure_ascii=False)

#данная функция формирует по входным параметрам запроса ищет данные в json файле и формирует словарь
def SearchToDict (path_input, search_for, search_for_attribute, search_output1, search_output2, main_cards_dict):
    output_main = {}
    output_main['Первый атрибут'] = []
    output_main['Второй атрибут'] = []
    for dtp_dicts in main_cards_dict:
        if dtp_dicts[search_for] == search_for_attribute:
            output_main['Первый атрибут'].append(dtp_dicts[search_output1])
            output_main['Второй атрибут'].append(dtp_dicts[search_output2])
    print (output_main)
    return output_main

def DictToCSV(output_main):
    dict = {}
    dict = output_main
    with open('dict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',)
        for line in dict.values():
            writer.writerow(line)


def main():
    output_main = {}
    path_input = 'chuck.json'#input('Укажите путь к загружаемому файлу:  ')
    search_for = 'DTP_V'#input ('Укажите что вы ищете (например - "DTP_V"):  ')
    search_for_attribute = 'Наезд на препятствие'#input('Введите с какими значениями нужно найти объект  ')
    search_output1 = 'District'#input('Введите первый атрибут данного объекта который вывести в файл  ')
    search_output2 = 'Time'#input('Введите второй атрибут данного объекта который вывести в файл  ')
    main_cards_dict = getJson(path_input)
    output_main = SearchToDict(path_input, search_for, search_for_attribute, search_output1, search_output2, main_cards_dict)
    DictToCSV(output_main)


main()