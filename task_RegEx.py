from enum import unique
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from typing import final
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def get_result_list(contacts_list, pattern, result_pattern):
  res_list = []

  for item in contacts_list:
    string_list = []
    for string in item:
      res = re.sub(pattern, result_pattern, string)
      string_list.append(res)
    res_list.append(string_list)
  
  return res_list

phone_changed = get_result_list(contacts_list, r'(\+?7|8)\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d+)[\s]?\(?(\w+\.?)[\s]?(\d{0,4})\)?', r'+7(\2)\3-\4-\5\6\7')
add_phone_changed = get_result_list(phone_changed, r'(\d{2})(\w{3})', r'\1 \2')

list_sum = []
name_list = []
name_string_list = []
for item in add_phone_changed:
  string = ','.join(item)
  name_changed = re.sub(r'(^\w+)[\s?,?](\w+)[\s?]?(\w+)?(,,,?)?', r'\1,\2,\3,', string)
  name_string = re.sub(r'(\w),,,(\w)', r'\1,\2', name_changed)
  name_string_list.append(name_string)
  string_list = name_string.split(',')
  list_sum.append(string_list)


test_list = []
for num in range(len(list_sum)):
  
  new_list = [x for i,x in enumerate(list_sum) if i!=num]
  for i in new_list:
    if i[0] == list_sum[num][0] and i[1] == list_sum[num][1]:
      list_a = list(enumerate(i))
      list_b = list(enumerate(list_sum[num]))
      list_a.extend(list_b)
      list_a = sorted(list(set(list_a)))
      test_list.append(list_a)


dict_info = {}
dict_list_sum = []
for i in test_list:
  dict_list = []
  for j in i:
    if j[0] not in dict_info:
      dict_info[j[0]] = j[1]
    elif j[0] in dict_info:
      if j[1] != '':
        dict_info[j[0]] = j[1]
  for i in dict_info:
    dict_list.append(dict_info[i])   
  dict_list_sum.append(dict_list)


double_list = []
for num in range(len(dict_list_sum)):
  new_dict_list = (x for i,x in enumerate(dict_list_sum) if i!=num)
  for i in new_dict_list:
    if i[0] == dict_list_sum[num][0] and i[1] == dict_list_sum[num][1]:
      double_string = ','.join(i)
  double_list.append(double_string)
set_list = list(set(double_list))

double_dict = {}
for i in set_list:
  name_string = i.split(',')
  double_dict[name_string[0]] = name_string


test_dict = {}
for i in list_sum:
  test_dict[i[0]] = i

test_dict.update(double_dict)

final_list = []
for value in test_dict.values():
  final_list.append(value)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(final_list)