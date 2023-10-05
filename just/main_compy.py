file_en = 'lang/en_US.lang'
file_ru = 'lang/ru_RU.lang'
file_new = 'lang/ru_RU_new.lang'

with open(file_en, 'r', encoding='UTF-8') as text_en:
    with open(file_ru, 'r', encoding='UTF-8') as text_ru:
        t_ru = list(text_ru)
        for i in text_en:
            for _ in t_ru:
                if i.strip().split('=')[0] == _.split('=')[0]:
                    i = i.strip().replace(i.strip().split('=')[1], _.strip().split('=')[1])
            print(i.strip())