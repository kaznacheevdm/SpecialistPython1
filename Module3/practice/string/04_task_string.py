# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

text = input("введите строку: ")
if text == "":
    text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
    print ("строка изменена на \n", text)


words = text.split()
i=0 # индекс элементов списка words
j=0 # счетчик слов,длина которых больше 5
while i < len(words):
    if len(words[i])>5:
        j+=1
    i+=1
print("Колличетво слов длиннее 5 символов равно",j)
