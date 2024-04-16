"""
Берётся перевод из новой версии мода. Если есть похожие команды до знака "=" из файла перевода, программа возьмет текст
который идёт после "=" из нового файла
и запишет в только что созданный (файл будет создан автоматически после запуска программы)
"""
old_file = r'lang\ru_RU.lang'
new_file = r'lang\ru_RU_new.lang'
result_file = r'lang\new.lang'


def comparator_complete():
    return "Complete"


if __name__ in "__main__":
    list_a = []
    list_b = []
    with open(old_file, 'r', encoding='UTF-8') as a:
        with open(new_file, 'r', encoding="UTF-8") as b:
            with open(result_file, 'a+', encoding='UTF-8') as result:
                result.truncate(0)  # - Очистка файла перед новой записью
                for text_a in a:
                    if '=' in text_a:
                        list_a.append(text_a.strip())
                for text_b in b:
                    if '=' in text_b and '#' not in text_b:
                        list_b.append(text_b.strip())
                for count, x in enumerate(list_a):
                    for y in list_b:
                        if x.split('=')[0] == y.split('=')[0]:
                            result.write(x.split('=')[0] + '=' + y.split('=')[1])
                            result.write(''.join('\n'))
                    print(count)

    print(comparator_complete())