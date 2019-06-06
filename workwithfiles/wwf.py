with open('referat.txt', 'r', encoding='utf-8') as f:
    count_lines = 0
    count_words = 0
    
    for line in f:
        count_words = count_words+len(line.split(' '))
        count_lines = count_lines + 1
        
    print ('Количество строк: ',count_lines)
    print('Количество слов: ', count_words)

with open('referat.txt', 'r', encoding='utf-8') as f2:
    content = f2.read()
    content_len = len(content)
    print('Длина строки: ',content_len)
    new_content = content.replace('.','!')
    # print(new_content)

with open('referat2.txt', 'w', encoding='utf-8') as f3:
    f3.write(new_content)
    