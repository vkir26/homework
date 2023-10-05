'''
Переводчик файлов minecraft
'''
import os

# Перевод для файлов lang
# file_en = 'lang/en_US.txt'
# file_ru = 'lang/ru_RU.txt'
# file_new = 'lang/ru_RU_new.txt'
#
# with open(file_en, 'r', encoding='UTF-8') as text_en:
#     with open(file_ru, 'r', encoding='UTF-8') as text_ru:
#         t_ru = list(text_ru)
#         for i in text_en:
#             for _ in t_ru:
#                 if _.strip().split(':') == i.strip().split(':') and len(i.strip().split(':')) != 1:
#                     print(i.strip().split(':')[1])

# Производим поиск предложений для перевода json

# file_en = 'C:/Users/vanya/Desktop/anvils.json'
# file_ru = 'C:/Users/vanya/Desktop/translate.txt'
# with open(file_en, 'r', encoding='UTF-8') as text_en:
#     with open(file_ru, 'w') as file:
#         for i in [i.strip() + '\n' for i in text_en if len(i.strip().split()) > 2]:
#             file.write(i)

# Конструктор перевода в конечный файл
# file_en = 'C:/Users/vanya/Desktop/anvils.json'
# file_ru = 'C:/Users/vanya/Desktop/translate.txt'
# n = 0
# with open(file_en, 'r', encoding='UTF-8') as text_en:
#     with open(file_ru, 'r', encoding='UTF-8') as text_ru:
#         t_ru = list(text_ru)
#         for i in text_en:
#             if len(i.split()) > 2:
#                 print(i.replace(i.split('":')[1], t_ru[n].split('":')[1]), end='\r')
#                 n += 1
#             else:
#                 print(i, end='\r')

# import os.path
#
# # Ищет все файлы в указанном пути и берёт из них текст для перевода, происходит редактирование и сортировка
# for root, dirs, files in os.walk("C:/Users/vanya/Desktop/field_guide/en_us"):
#     for filename in files:
#         file_en = os.path.join(root, filename).replace("\\", '/')
#         file_ru = 'C:/Users/vanya/Desktop/translate.txt' # - путь для записи текста
#         with open(file_en, 'r', encoding='UTF-8') as text_en:
#             with open(file_ru, 'w+', encoding='UTF-8') as file:
#                 for i in [i.strip() + '\n' for i in text_en if len(i.strip().split()) > 2]:
#                     file.write(i)

# КОПИЯ №1
# import os.path
# import time
#
# # Ищет все файлы в указанном пути и берёт из них текст для перевода, происходит редактирование и сортировка
# for root, dirs, files in os.walk("C:/Users/vanya/Desktop/field_guide/en_us"):
#     for filename in files:
#         file_en = os.path.join(root, filename).replace("\\", '/')
#         file_ru = 'C:/Users/vanya/Desktop/translate.txt' # - путь для записи текста
#         with open(file_en, 'r', encoding='UTF-8') as text_en:
#               with open(file_ru, 'w+', encoding='UTF-8') as file:
#                 for i in [i.strip() + '\n' for i in text_en if len(i.strip().split()) > 2]:
#                     #file.write(i)
#                     pass
#
#         n = 0 # Счётчик (Чтобы перевод не повторялся, прибавляем в срезе каждую операцию на +1)
#         with open(file_en, 'r', encoding='UTF-8') as text_en:
#             with open(file_ru, 'r', encoding='UTF-8') as text_ru:
#                 t_ru = list(text_ru)
#                 for i in text_en:
#                     if len(i.split()) < 1:
#                         print(i.replace(i.split('":')[1], t_ru[n].split('":')[1]).rstrip())
#                         n += 1
#                     else:
#                         print(i.rstrip())

import os.path

file_ru = 'C:/Users/vanya/Desktop/translate.txt'  # - путь для записи текста и дальнейшего перевода
file = 'C:/Users/vanya/Desktop/field_guide/en_us'  # - Путь до файлов, которые необходимо перевести


# def func_entry():
#     # Ищет все файлы в указанном пути и берёт из них текст для перевода, для его редактирования
#     for root, dirs, files in os.walk(file):
#         for filename in files:
#             file_en = os.path.join(root, filename).replace("\\", '/')
#             with open(file_en, 'r', encoding='UTF-8') as text_en:
#                 with open(file_ru, 'a+', encoding='UTF-8') as file_translate:  # Файл который должен содержать текст для перевода
#                     for t_redact in [t_redact.strip() + '\n' for t_redact in text_en if len(t_redact.strip().split()) > 2]:
#                         if len(t_redact.split()) > 2 and len(t_redact.split('":')) == 2:
#                             # file_translate.write(t_redact.strip() + '\n')
#                             pass

def func_entry():
    # Ищет все файлы в указанном пути и берёт из них текст для перевода, для его редактирования
    for root, dirs, files in os.walk(file):
        for filename in files:
            file_en = f'{root.strip()}/{filename.strip()}'
            with open(file_en, 'r', encoding='UTF-8') as text_en:
                with open(file_ru, 'a+', encoding='UTF-8') as file_translate:  # Файл который должен содержать текст для перевода
                    for t_redact in [t_redact.strip() + '\n' for t_redact in text_en if len(t_redact.strip().split()) > 2]:
                        if len(t_redact.split()) > 2 and len(t_redact.split('":')) == 2:
                            file_translate.write(t_redact.strip() + '\n')


def func_assembly():
    pass


if __name__ == "__main__":
    func_entry()
    # func_assembly()