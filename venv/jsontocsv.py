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
 #   def SearchToDict (path_input, search_for, search_for_attribute, search_output1, search_output2, main_cards_dict):
 #       output_main['Первый атрибут'] = []
 #       output_main['Второй атрибут'] = []
 #       for dtp_dicts in main_cards_dict:
 #           if dtp_dicts[search_for] == search_for_attribute:
 #               output_main['Первый атрибут'].append(dtp_dicts[search_output1])
 #               output_main['Второй атрибут'].append(dtp_dicts[search_output2])
 #       print (output_main)
 #       return output_main

def JsonToTable(path_input, main_cards_dict, label):
    output_list1 = [] #ключи
    output_list2 = [] #значения
    for dtp_dicts in main_cards_dict:
        for keys in dtp_dicts.keys():
            if keys == 'infoDtp':
                for subkeys in dtp_dicts[keys].keys():
                    if subkeys == 'ts_info':
                        for ts_info_key in list(dtp_dicts[keys][subkeys][0].keys()):
                            if ts_info_key == 'ts_uch':
                                if dtp_dicts[keys][subkeys][0]['ts_uch']: #проверка на заполненность атрибута ts_uch. в некоторых карточках он пуст
                                    for ts_uch_key in list(dtp_dicts[keys][subkeys][0][ts_info_key][0].keys()):
                                        output_list2.append(str(dtp_dicts[keys][subkeys][0][ts_info_key][0][ts_uch_key]) + ' ' + str(dtp_dicts[label]))
                                        output_list1.append(str(keys) + ' ' + str(subkeys) + ' ' + str(ts_info_key) + ' ' + str(ts_uch_key))
                            else:
                                output_list2.append(dtp_dicts[keys][subkeys][0][ts_info_key]+' ' + str(dtp_dicts[label]))
                                output_list1.append(str(keys) + ' '+ str(subkeys) + ' ' + str(ts_info_key))
                    else:
                        output_list2.append(str(dtp_dicts[keys][subkeys])+' '+ str(dtp_dicts[label]))
                        output_list1.append(str(keys) + ' '+ str(subkeys))
            else:
                output_list2.append(str(dtp_dicts[keys]) +' '+ str(dtp_dicts[label]))
                output_list1.append(keys)
    return output_list2




def DictToCSV(output_main):
    dict = {}
    dict = output_main
    with open('dict.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',)
        for line in dict.values():
            writer.writerow(line)

def SearchInList (SearchIt, List):
    output_list = []
    for element in List:
        spl_element = element.split()[0]
        if SearchIt == spl_element:
            output_list.append(element.split()[1])
    print (output_list)



def main():
    output_main = {}
    path_input = input('Укажите путь к загружаемому файлу:  ')
    in_label = input ('Укажите что Вы ищете ')
    search_for = input ('Укажите по какому параметру:  ')
    main_cards_dict = getJson(path_input)
    output_main = JsonToTable(path_input, main_cards_dict, in_label)
    SearchInList(search_for, output_main)


main()