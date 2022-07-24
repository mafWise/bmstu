#Функция дополненной проверки строки на числовую значимость

from typing import Text


def word_input(sentence):
        while True:
            word = input(sentence)
            if word not in ' .:;,!?-':
                break
            print('Неверный ввод')
        return word 

def isDigit(t):
    if t == '': return False
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

def reset():
    global text
    for j in range(len(text)):
        i = 0
        while i <= len(text[j]) - 1:
            if text[j][i] == ' ' and text[j][i + 1] != ' ': pass
            elif text[j][i] == ' ':
                text[j] = text[j][:i] + text[j][i + 1:]
                continue
            i += 1    
        text[j] = text[j].strip()
        
#Функция ввода строки и проверка ее на числовую значимость
def digit_input(stroke):
    while True:
        n = input(stroke).strip()
        if isDigit(n) == True and float(n) > 0:
            return int(float(n))
        print('Введенный символ не является числом или является числом не положительным. Повторите ввод')

def main_transformation(key):
    global text, max_len_stroke
    if key == 1:
        reset()

    if key == 2:
        reset()
        for i in range(len(text)):
            if len(text[i]) == max_len_stroke:
                continue
            diff = max_len_stroke - len(text[i])
            #Учитывать или не учитывать знаки
            # if text[i][-1] not in symbols: diff -= 1
            text[i] = ' ' * diff + text[i]
    
    elif key == 3:
        reset()
        for i in range(len(text)):
            if len(text[i]) == max_len_stroke:
                continue
            diff = (max_len_stroke - len(text[i])) // text[i].count(' ') + 1
            diff_add = (max_len_stroke - len(text[i])) % text[i].count(' ')
            j = 0
            while j != len(text[i]):
                if text[i][j] == ' ':
                    m = ' ' if diff_add > 0 else ''
                    text[i] = text[i][:j] + ' ' * diff + m + text[i][j + 1:]
                    d = 1 if diff_add > 0 else 0
                    j += diff - 1 + d
                    diff_add -= 1
                j += 1
    for s in text: print(s)

text = [
    'Я помню чудное 1 - 1 мгновенье:',
    'Передо мной явилась ты,',
    'Как мимолетное виденье,',
    'Как гений 54 + 1 чистой красоты.',

    'В томленьях грусти безнадежной,',
    'В тревогах шумной суеты,',
    'Звучал мне долго голос нежный',
    'И снились милые черты.',

    'Шли годы. 1-121 Бурь порыв мятежный 100-1000000',
    'Рассеял прежние мечты,',
    'И я забыл твой голос нежный,',
    'Твои небесные черты.',

    'В глуши, во мраке заточенья',
    'Тянулись тихо 1 + 4 дни мои',
    'Без божества, без вдохновенья,',
    'Без слез, без жизни, без любви.',

    'Душе настало пробужденье:',
    '5 - 1 И вот опять явилась ты,',
    'Как мимолетное 6 + 2 виденье,',
    'Как гений 1+2 чистой красоты.',
]

variants = (
    'Выровнять текст по левому краю',
    'Выровнять текст по правому краю',
    'Выровнять текст по ширине',
    'Удаление заданного слова',
    'Замена одного слова другим во всём тексте',
    'Вычисление арифметических выражений (+ и -)',
    'Найти и напечатать предложения, в которых количество слов совпадает' 
)

size = 120
symbols = ',.:;?!-'
dig = []
check = 0
max_len_stroke = len(max(text, key=len))
RAM = 1
for i in text: print(i)

while True:
    print('\n|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    for i in range(len(variants)):
        print('|' + '{:^4}|'.format(i + 1) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
        print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    
    var = digit_input('Введите номер варианта: ')

    if var == 1:
        main_transformation(1)
        RAM = 1

    elif var == 2:
        main_transformation(2)
        RAM = 2

    elif var == 3:
        main_transformation(3)
        RAM = 3


    elif var == 4:
        reset()
        word = word_input('Введите слово: ')
        for i in range(len(text)): text[i] = text[i].replace(word, '')
        main_transformation(RAM)

    elif var == 5:
        reset()
        word = input('Введите новое слово: ')
        word1 = word_input('Введите заменяемое слово: ')
        for i in range(len(text)): text[i] = text[i].replace(word1, word)
        main_transformation(RAM)  

    elif var == 6:
        for i in range(len(text)):
            while '+' in text[i] or '-' in text[i]:
                sign_id = text[i].index('+') if '+' in text[i] else text[i].index('-')
                sign = text[i][sign_id]

                if text[i][sign_id - 1] != ' ' and text[i][sign_id + 1] != ' ':
                    text[i] = text[i][:sign_id] + ' ' + text[i][sign_id: sign_id + 1] + ' ' + text[i][sign_id + 1:]
                elif text[i][sign_id - 1] != ' ' and text[i][sign_id + 1] == ' ':
                    text[i] = text[i][:sign_id - 1] + ' ' + text[i][sign_id - 1: ]
                elif text[i][sign_id - 1] == ' ' and text[i][sign_id + 1] != ' ':
                    text[i] = text[i][sign_id + 1:] + ' ' + text[i][:sign_id + 1]
                stroke = text[i].split()
                
                sign_id = stroke.index(sign)
                
                ans = int(stroke[sign_id - 1]) + int(stroke[sign_id + 1]) if stroke[sign_id] == '+' else \
                      int(stroke[sign_id - 1]) - int(stroke[sign_id + 1])
                del stroke[sign_id + 1]
                del stroke[sign_id]
                del stroke[sign_id - 1]
                ans = str(ans) if ans >= 0 else '{' + str(ans)[1:]
                stroke.insert(sign_id - 1, '(' + ans + ')')
                text[i] = ' '.join(stroke)
            text[i] = text[i].replace('{', '-')
        main_transformation(RAM)

    elif var == 7:
        strokes_len = set([])
        strokes_len_all = []
        for i in range(len(text)):
            s = len(text[i].split())
            strokes_len.add(s)
            strokes_len_all.append(s)

        for s in strokes_len:
            print('\n\nСтроки с количеством слов: {}'.format(s))
            for z in range(len(strokes_len_all)):
                if s == strokes_len_all[z]:
                    print(text[z])


    input('\nНажмите Enter для продолжения...')