from tkinter import *
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.misc import derivative

from numpy import arange
import numpy as np
from math import *

def func(x):
    return eval(y.get().replace("x", str(x)))

def graph():
    x = arange(float(a.get()), float(b.get())+0.1, 0.1)
    f = np.array([func(i) for i in x])
    
    plt.plot(x, f)
    plt.grid()

    res_min = list(argrelextrema(f, np.less)[0])
    for dot in res_min:
        #print(x[dot], f[dot])
        plt.scatter(x[dot], f[dot], color='red', s=40, marker='o')
    

    res_max = list(argrelextrema(f, np.greater)[0])
    for dot in res_max:
        #print(x[dot], f[dot])
        plt.scatter(x[dot], f[dot], color='red', s=40, marker='o')

    inf = []
    for i in x:
        if abs(derivative(func, i, n = 2)) < 1e-8:
            plt.scatter(i, func(i), color='purple', s=40, marker='o')

    d = plt.scatter(0, 0, color='red', s=40, marker='o', Label = 'экстремум')
    d2 = plt.scatter(0, 0, color='orange', s=40, marker='o', Label = 'корень')
    d3 = plt.scatter(0, 0, color='purple', s=40, marker='o', Label = 'точка перегиба')
    draw_table()
    #d.set_label('экстремум')
    plt.legend()
    d.remove()
    d2.remove()
    d3.remove()
    plt.show()

def draw_table():
    global table
    try:
        table.destroy()
    except:
        pass
    table = Frame(window, width = 200, height = 50)
    table.pack()

    header = ["№ корня", "[x(i);x(i+1)]", "x'", "f(x')",
          "Количество\nитераций", "Код ошибки"]

    c = 0
    for column in header:
        Label(table, width = 12, text = column,
              anchor = 'w').grid(row = 7, column = c, sticky=NSEW)
        c += 1

    counter = 1
    r = 8

    try:
        start = float(a.get())
        step = float(h.get())
        stop = start + step
        final = float(b.get())
        nmax = int(Nmax.get())
        e = float(eps.get())
    except:
        exit

    while stop - step - final < 1e-8:
        res = sec(start, stop, e, nmax)
        
        if len(res) != 2:
            res[0] = '{:.4f}'.format(res[0])
            res[1] = '{:.4f}'.format(res[1])
            tmp = [str(counter), "["+'{:.2f}'.format(start)+";"+'{:.2f}'.format(stop)+"]"] + res
            #print(tmp)
            c = 0
            if tmp[-1] == '0':
                for data in tmp:
                    Label(table, width = 12, text = data,
                  anchor = 'w').grid(row = r, column = c, sticky=NSEW)
                    c += 1
                    d = plt.scatter(float(tmp[2]), float(tmp[3]), color='orange', s=40, marker='o')
                    
            else:
                for data in tmp:
                    Label(table, width = 12, text = data,
                  anchor = 'w').grid(row = r, column = c, sticky=NSEW)
                    c += 1
                    d = plt.scatter(float(tmp[2]), float(tmp[3]), color='orange', s=40, marker='o')
    
            r += 1
            counter += 1
            #print(res)
        start += step
        stop += step
    #d = plt.scatter(0, 0, color='orange', s=40, marker='o', Label = 'корень')
    #d.set_label('корень')
    #d.remove()

def sec(x1, x2, eps, nmax):
    y1, y2=func(x1), func(x2)
    
    if y1 * y2 > 0:
        return ['there_is_no_root', 0]

    xx = x2
    n = 0;

    while n < nmax:
        n += 1
        x3=(abs(y2)*x1+abs(y1)*x2)/(abs(y2)+abs(y1))
        y3=func(x3)
        if y1*y3 < 0: 
            x2, y2 = x3, y3
        else: 
            x1, y1 = x3, y3
        if abs(x3 - xx) < eps:
            return [x3, y3, n, 0]
        xx = x3
    return [x3, y3, n, 1]

window = Tk()
window.title("lab2")

inputs = Frame(window, width = 100, height = 50)
inputs.pack()

datas = ["y", "a", "b", "h", "Nmax", "eps"]

r = 0
for data in datas:
    Label(inputs, width = 18, text = data + " = ",
      anchor = 'e').grid(row = r, column = 0)
    exec(data +"=Entry(inputs)")
    eval(data + ".grid(row = r, column = 1)")
    r += 1

table = Frame(window, width = 200, height = 50)

Label(window, text = 'Расшифровка кодов ошибок:\n0 - нет ошибок\n1 - выход за nmax').pack()

#Button(inputs, text="graph", command = graph).grid(row = 6, column = 1)
Button(inputs, text="graph", command = lambda: [table.destroy(), graph()]).grid(row = 6, column = 1)

window.mainloop()
Label(tableframe, text = "f(x')", relief = GROOVE, width = 17).grid(row = 1, column = 3)
Label(tableframe, text = 'Количество итераций', relief = GROOVE, width = 26).grid(row = 1, column = 4)
Label(tableframe, text = 'Код ошибки', relief = GROOVE, width = 17).grid(row = 1, column = 5)

Label(tableframe, text = '[{:^9.3}, {:^9.3}]'.format(str(a-step), str(a)), relief = GROOVE, width = 17).grid(row = i+2, column = 1)
Label(tableframe, text = '{:^12.6f}'.format(x_roots[i]),\
                     relief = GROOVE, width = 17).grid(row = i+2, column = 2)
Label(tableframe, text = '{:^12.6f}'.format(y_roots[i]),\
                     relief = GROOVE, width = 17).grid(row = i+2, column = 3)
Label(tableframe, text = iters_arr[i], relief = GROOVE, width = 26).grid(row = i+2, column = 4)
Label(tableframe, text = errors[i], relief = GROOVE, width = 17).grid(row = i+2, column = 5)

window = Tk()
window.title('Анализ графика')
window.geometry('1250x500+100+200')
mainframe = Frame(window)
mainframe.pack(side = TOP, fill = X)
tableframe = Frame(window)
tableframe.pack(side = BOTTOM, fill=BOTH, expand = 1)
Label(mainframe, text = "Функция в виде 'f(x)'").grid(row = 0, column = 0)
input_func = Entry(mainframe, width = 25)
input_func.grid(row=1, column = 0)
Label(mainframe, text = 'Начало отрезка').grid(row = 0, column = 1)
input_start = Entry(mainframe)
input_start.grid(row = 1, column = 1)
Label(mainframe, text = "Конец отрезка").grid(row = 0, column = 2)
input_stop = Entry(mainframe)
input_stop.grid(row=1, column = 2)
Label(mainframe, text = 'Шаг').grid(row = 0, column = 3)
input_step = Entry(mainframe)
input_step.grid(row = 1, column = 3)
Label(mainframe, text = "Максимальное число итераций").grid(row = 0, column = 4)
input_Nmax = Entry(mainframe, width = 30)
input_Nmax.grid(row=1, column = 4)
Label(mainframe, text = 'Точность').grid(row = 0, column = 5)
input_eps = Entry(mainframe)
input_eps.grid(row = 1, column = 5)
but_table = Button(mainframe, text = 'Вывести таблицу', command = lambda: data_check('table'))
but_graph = Button(mainframe, text = 'График', command = lambda: data_check('graph'))
but_table.grid(row = 2, column = 2)
but_graph.grid(row = 2, column = 4)


window.mainloop()
