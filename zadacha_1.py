# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'По окончании забвнятий, в положенный срок, я абвыл приписан ' \
       'в качестве ассистента хирурга к Пятому Нортумабверлендскому ' \
       'стрелкоабввому полку. Мой полк в то время стоял в Индии, и, ' \
       'прежде чем я прибыл на место службы, началась Вторабвя ' \
       'афганская кампания.'

list_text = text.split()
nnn = []
for i in range(len(list_text)-1):
       if 'абв' in list_text[i]:
              nnn.append(i)

new_text_list = []
for i in range(len(list_text)):
       if i not in nnn:
              new_text_list.append(list_text[i])
print(new_text_list)
new_text = ' '.join(str(x) for x in new_text_list)
print(new_text)

