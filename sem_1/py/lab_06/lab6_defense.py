def is_digit_ver_2_0(t):
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

s = []

while True:
    n = input('Введите количество элементов')
    if is_digit_ver_2_0(n) == True:
        break
n = int(float(n))

for i in range(n):
    while True:
        a = input()
        if is_digit_ver_2_0(a) == True:
            break
    a = float(a)
    s.append(a)

for j in range(n):
    print(s[j])
    if s[j] == 0:
        del s[j]
        s.append(0)
print(s)

