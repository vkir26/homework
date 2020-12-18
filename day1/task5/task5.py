# file = open('task5_data.txt', 'r', encoding='UTF-8')
# print(file.read())
# file.close()
# with open('task5_data.txt', 'rb') as file:
#         arr = bytearray(i for i in file.read())
#         print(arr)

# file = open('task5_data.txt', 'rb+')
# text = file.read()
# bin(text)
# print(int(text.hex(), 16))

# file = open('task5_data.txt', 'rb+')
# text = file.read()
# print(text)
# print(bin(int(text.hex(), 16))[2:])

# text = 'Привет'.encode()
# print(text) # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# print(bin(int(text.hex(), 16))[2:])
# print(bytes.decode(text))

# text = (b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82').decode('UTF-8')
# print(text)

# s = str(0b100).encode('UTF-8')
# print(int(s.decode('UTF-8')))

# file = open('task5_data.txt', 'rb')
# text = file.read()
# print(text)
# print(bin(int(text.hex(), 16))[2:])
# print(text.decode('UTF-8'))

# file = open('task5_data.txt', 'rb+')
# text = file.read()
# print(bin(int(text.hex(), 16))[2:])
# print(text)

# text = ''
# print(bytes.fromhex(hex(int(text, 2))[2:]).decode(encoding="utf-8"))

# file = open('task5_data.txt', 'rb+')
# text = file.read()
# print(bin(int(text.hex(), 16))[2:].zfill(8))

#print(bin(int(text.hex(), 16))[2:])
# print(bin(int(text.hex(), 16))[2:]
# file_2 = open('task5_data_new.txt', 'ab+')
# text = file.read())
# print(text)

x = 1
y = 6
z = x ^ y
print(z)