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
        return cards_dict

def JsonToTable(path_input, main_cards_dict, label):
    output_list1 = [] #ключи
    output_list2 = [] #значения
    index = 0 #индекс который присваивает каждой карточке ДТП уникальный номер
    for dtp_dicts in main_cards_dict:
        index += 1
        for keys in dtp_dicts.keys():
            if keys == 'infoDtp':
                for subkeys in dtp_dicts[keys].keys():
                    if subkeys == 'ts_info':
                        for ts_info_key in list(dtp_dicts[keys][subkeys][0].keys()):
                            if ts_info_key == 'ts_uch':
                                if dtp_dicts[keys][subkeys][0]['ts_uch']: #проверка на заполненность атрибута ts_uch. в некоторых карточках он пуст
                                    for ts_uch_key in list(dtp_dicts[keys][subkeys][0][ts_info_key][0].keys()):
                                        output_list2.append(str(dtp_dicts[keys][subkeys][0][ts_info_key][0][ts_uch_key]) + ' ' + str(dtp_dicts[label])+ ' ' + str (index))
                                        output_list1.append(str(keys) + ' ' + str(subkeys) + ' ' + str(ts_info_key) + ' ' + str(ts_uch_key))
                            else:
                                output_list2.append(dtp_dicts[keys][subkeys][0][ts_info_key]+' ' + str(dtp_dicts[label])+ ' ' + str (index))
                                output_list1.append(str(keys) + ' '+ str(subkeys) + ' ' + str(ts_info_key))
                    else:
                        output_list2.append(str(dtp_dicts[keys][subkeys])+' '+ str(dtp_dicts[label])+ ' ' + str (index))
                        output_list1.append(str(keys) + ' '+ str(subkeys))
            else:
                output_list2.append(str(dtp_dicts[keys]) +' '+ str(dtp_dicts[label]) + ' ' + str (index))
                output_list1.append(keys)
    return output_list2


def DictToCSV(output_main):
    dict = {}
    dict = output_main
    with open('dict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',)
        for line in dict.values():
            writer.writerow(line)

def SearchInList (SearchIt, SearchIt2, SearchIt3, SearchIt4, List):
    output_list = []
    output_list2 = []

    res_list = []
    for element in List:
        spl_element = element.split()[0]
        if (spl_element == SearchIt) or  (spl_element == SearchIt2) or (spl_element == SearchIt3) or (spl_element == SearchIt4):
            output_list.append(element)

    for element in output_list:
        spl_element = element.split()[-1]
        for element2 in output_list:
            spl_element2 = element2.split()[-1]
            if spl_element == spl_element2:
                output_list2.append(element.split()[-2])


    print (set(output_list2))


def main():
    output_main = {}
    path_input = input('Укажите путь к загружаемому файлу:  ')
    in_label = input ('Укажите что Вы ищете ')
    search_for = input ('Укажите по какому параметру:  ')
    search_for2 = input('Укажите второй параметр:  ')
    search_for3 = input('Укажите третий параметр:  ')
    search_for4 = input('Укажите четвертый параметр:  ')

    main_cards_dict = getJson(path_input)
    output_main = JsonToTable(path_input, main_cards_dict, in_label)
    SearchInList(search_for, search_for2, search_for3, search_for4, output_main)


main()