import tkinter as tk
from tkinter import Label, StringVar, messagebox, Menu


window = tk.Tk()

window.title("Калькулятор")

tk.Label(text='', background='white', width=25).place(x=90,y=260)


var = StringVar()
message_entry = tk.Entry(width=25, textvariable=var)
message_entry.place(x=90,y=100)

M = 3
eps = 6

# Очистка поля вывода ---------------------------------------------------------------------

def clear_output():
    tk.Label(text='', background='white', width=25).place(x=90,y=260)

# Очистка поля ввода ----------------------------------------------------------------------

def clear_input():
    message_entry.delete(0, tk.END)

# Вывод информации о программе ------------------------------------------------------------

def show_info():
    msg = "Данная программа предназначена для перевода\n\
вещественных чисел из 10-ой в 3-ую систему счисления и обратно\n\
Автор: Турчанский Никита ИУ7-24Б"
    messagebox.showinfo("Информация", msg)

# Вывод ошибки на экран -------------------------------------------------------------------

def show_error():
    messagebox.showerror("Ошибка", "Введено некорректное значение")
counter = 0

# Добавление символа в строку ввода нажатием кнопки на виджете ----------------------------

def add(sim):
    global counter
    if sim == '-':
        counter += 1
        if counter % 2 == 0:
            message_entry.delete(0)
            return 0
        message_entry.insert(0, '-')
                
    else:
        message_entry.insert(tk.END, sim)

# Функция проеврки числа и последующий вызов ф-ций перевода -------------------------------

def check(a, dis):
    try: 
        var = float(a)
    except: 
        show_error()
        return 2
    ans = ''
    min = False
    if var < 0:
        var *= -1
        min = True
    var = str(var).split('.')
    if dis == '10':
        for i in range(3,10):
            if var[0].count(str(i)) >= 1 or var[1].count(str(i)) >= 1:
                show_error()
                return 2
        ans = into_10(var)
    else:
        ans = into_3(var)
    f = 1
    if min == True:
        f = -1

    tk.Label(text=f"{float(ans)*f:f}", background='white', width=20).place(x=115,y=260)

# Перевод числа в 10-ую систему ----------------------------------------------------------- 

def into_10(var):
    def convert_int(a):
        ans = 0
        for i in range(1, len(a) + 1):
            ans += int(a[-1*i]) * 3 ** (i-1)
        return ans
    def convert_compl(b):
        ans = 0
        for i in range(len(b)):
            ans += int(b[i]) * 3 ** -(i + 1)
        return ans
    return convert_int(var[0]) + convert_compl(var[1])

# Перевод числа в 3-ую систему ------------------------------------------------------------

def into_3(var):
    
    def convert_int(a):
        first='0'
        while a // M >= 1:
            first += str(a%M)
            a //= M
        first += str(a)
        return str(first[1:][::-1])
    def convert_compl(b):
        second = float('0.' + b)
        ans = ''
        for i in range(eps):
            second = second * M
            ans += str(int(second))
            second = second % 1
        return ans
    return convert_int(int(var[0])) + '.' + convert_compl(var[1])


# Настройка окна --------------------------------------------------------------------------

window.columnconfigure(0, minsize=450)
window.rowconfigure(0, minsize=200)
window.resizable(width=False, height=False)
 

# Создание кнопок с цифрами ---------------------------------------------------------------

tk.Button(text="1", width=5, command=lambda: add('1')).grid(row=3, column=0, sticky="se")
tk.Button(text="4", width=5, command=lambda: add('4')).grid(row=4, column=0, sticky="se")
tk.Button(text="7", width=5, command=lambda: add('7')).grid(row=5, column=0, sticky="se")
tk.Button(text=".", width=5, command=lambda: add('.')).grid(row=6, column=0, sticky="se")

tk.Button(text="2", width=5, command=lambda: add('2')).grid(row=3, column=1, sticky="se")
tk.Button(text="5", width=5, command=lambda: add('5')).grid(row=4, column=1, sticky="se")
tk.Button(text="8", width=5, command=lambda: add('8')).grid(row=5, column=1, sticky="se")
tk.Button(text="0", width=5, command=lambda: add('0')).grid(row=6, column=1, sticky="se")
 
tk.Button(text="3", width=5, command=lambda: add('3')).grid(row=3, column=2, sticky="se")
tk.Button(text="6", width=5, command=lambda: add('6')).grid(row=4, column=2, sticky="se")
tk.Button(text="9", width=5, command=lambda: add('9')).grid(row=5, column=2, sticky="se")
tk.Button(text="-", width=5, command=lambda: add('-')).grid(row=6, column=2, sticky="se")

tk.Button(text="Информация", width=22, command=lambda: show_info()).grid(row=0, column=0, sticky="ne", columnspan=3)
tk.Button(text="Очистить поле ввода", width=22, command=lambda: clear_input()).grid(row=1, column=0, sticky="ne", columnspan=3)
tk.Button(text="Очистить поле вывода", width=22,command=lambda: clear_output()).grid(row=2, column=0, sticky="ne", columnspan=3)

# Создание меню ---------------------------------------------------------------------------

main_menu = Menu()
main_menu.add_command(label="Информация", command=lambda: show_info())
main_menu.add_command(label="Очистить поле ввода", command=lambda: clear_input())
main_menu.add_command(label="Очистить поле вывода", command=lambda: clear_output())
window.config(menu=main_menu)

# Создание названий и основных кнопок для преобразований ----------------------------------

tk.Label(text='Поле ввода').place(x=150,y=79)
tk.Label(text='Поле вывода').place(x=145,y=235)
tk.Button(text='Перевод в 10-ую', width=15, height=2, command=lambda: check(var.get(),'10'))\
    .place(x=30, y=160)
tk.Button(text='Перевод в 3-ую', width=15, height=2, command=lambda: check(var.get(),'3'))\
    .place(x=200,y=160)


window.mainloop()


