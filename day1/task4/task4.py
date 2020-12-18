file = open('task4_data.html', 'r')
text = file.read()
file_ascii = open('task4_ascii.html', 'w', encoding='ascii', errors='ignore')
file_ascii.write(text)
open('task4_data.html', 'r').read()
body, sep, tail = text.partition('<H1>')
with open('task4_body.html', 'w') as file_body:
    print(body.strip() + '\n</BODY>\n</HTML>', file=file_body)

#===========================================================
# file = open('task4_data.html', 'r', encoding='UTF-8')
# text = file.read()
# index = 2
# line = text[:index] + text[index+1:]
# print(line)

# text = '<p>Hello, World!!!</p>'
# head, sep, tail = text.partition(',')
#
# print(head)

# s = open('task4_data.html', 'r')
# text = s.read()
# head, sep, tail = text.partition('<H1>')
# with open('task4_body.html', 'w') as f:
#     print(head.strip() + '\n</BODY>\n</HTML>', file=f)

# <BODY>
# <p>Hello, World!!!</p>
# </BODY>