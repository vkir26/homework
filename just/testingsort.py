import re
import os
from googletrans import Translator


# def xml_main_translator():
#     # Указываем пути до файлов patch (оригинал), new_patch (будет создан тот же файл, но по другому пути)
#     path = r'C:\Users\vanya\Desktop\modules\MinecraftSpecialRules.xml'
#     new_path = r'C:\Users\vanya\Desktop\modules2\MinecraftSpecialRules.xml'
#     # Зададим переменную библиотеке перевода
#     translator = Translator()
#     # На какой язык переводим?
#     language = 'ru'
#
#     # Открываем файл для перевода в режиме чтения
#     with open(path, 'r', encoding='UTF-8') as file:
#         text = file.read()
#
#         # Здесь будут замены (уже с переводом)
#         replacements = []
#
#         # Зададим шаблон, который будем использовать для поиска нужных строк перевода
#         pattern = r'<Description[^>]*>([^<]*)</Description>'
#         # Ищем строки для замены используя шаблон выше
#         lines = re.findall(pattern, text)
#
#         for i in lines:
#             if i in text:
#                 # Сделаем запись нужных строк в список, здесь же переведём их на необходимый язык
#                 replacements.append(translator.translate(i, dest=language).text)
#         for line in replacements:
#             # Производим замену
#             text = re.subn(pattern, f"<Desc>{line}</Desc>", text, 1)[0]
#         # Делаем запись в новый файл
#         with open(new_path, 'a+', encoding='UTF-8') as new_file:
#             new_file.write(text.replace('<Desc>', '<Description>').replace('</Desc>', '</Description>'))
#
#         return "Successfully translated"
#
#
# print(xml_main_translator())


# Указываем пути до файлов patch (оригинал), new_patch (будет создан тот же файл, но по другому пути)
path = r'C:\Users\vanya\Desktop\cog_config'
for root, dirs, files in os.walk(path):
    for filename in files:
        # new_path = r'C:\Users\vanya\Desktop\modules2'
        # Зададим переменную библиотеке перевода
        translator = Translator()
        # На какой язык переводим?
        language = 'ru'

        # Открываем файл для перевода в режиме чтения
        with open(f"{path}/{filename}", 'r', encoding='UTF-8') as file:
            text = file.read()

            # Здесь будут замены (уже с переводом)
            replacements = []

            # Зададим шаблон, который будем использовать для поиска нужных строк перевода
            pattern = r'<Description[^>]*>([^<]*)</Description>'
            # Ищем строки для замены используя шаблон выше
            lines = re.findall(pattern, text)

            for i in lines:
                if i in text:
                    # Сделаем запись нужных строк в список, здесь же переведём их на необходимый язык
                    replacements.append(translator.translate(i, dest=language).text)
            for line in replacements:
                # Производим замену
                text = re.subn(pattern, f"<Desc>{line}</Desc>", text, 1)[0]
            # Делаем запись в новый файл
            with open(f"{path}2/{filename}", 'a+', encoding='UTF-8') as new_file:
                new_file.write(text.replace('<Desc>', '<Description>').replace('</Desc>', '</Description>'))