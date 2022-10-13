# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(text)
from itertools import groupby

list_t = [list(g) for k, g in groupby(text)]
str_res = ''
for i in list_t:
    str_res += str(len(i)) + i[0]
print(str_res)
#раскодирование:
import re
pattern_numbers = r'\d+'
number = re.findall(pattern_numbers,str_res)
print(number)

pattern_lit = r'\D'
letter = re.findall(pattern_lit,str_res)
print(letter)
str_res2=''
for i in range(len(number)):
    str_res2+= letter[i]*int(number[i])
print(str_res2)



