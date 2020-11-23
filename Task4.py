text = input('Введите текст через пробел: ')
words = text.split()
for ind, el in enumerate(words,1):
    print(ind,el[0:10])
