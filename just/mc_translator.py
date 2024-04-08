"""
Переводчик модов minecraft 1.7.10
"""

from googletrans import Translator
import os

file = r'lang\en_US.lang'
new_file = r'lang\ru_RU.lang'


# def translator_func():
#     translator = Translator()
#
#     absolute_path = os.path.abspath(file)
#     with open(absolute_path, 'r') as f:
#         for count, i in enumerate(f.readlines(), start=1):
#             with open(absolute_path.replace(file, new_file), 'a+', encoding="UTF-8") as ru_file:
#                 if len(i.split('=')) != 1:
#                     text = i.replace(i.split('=')[1], translator.translate(i.split('=')[1], dest='ru').text)
#                     ru_file.write(f"{text.strip()}\n")
#                 else:
#                     ru_file.write(f"{i.strip()}\n")
#                 print(count)
#     return 'Complete'
#
#
# print(translator_func())

translator = Translator()
print(translator.translate("HELLO", dest='ru'))