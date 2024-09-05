from pprint import pprint
""" чтение файла"""
def reading(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    return file.read()
    file.close()
"""перезапись файла"""
def writing(file_name, text):
    file = open(file_name, 'w', encoding = 'utf-8')
    return file.write(text)
    file.close()
"""запись текста в конец"""
def appending(file_name, text):
    file = open(file_name, 'a', encoding = 'utf-8')
    return file.write(text)
    file.close()


