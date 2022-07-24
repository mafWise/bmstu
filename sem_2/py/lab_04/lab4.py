from tkinter import *
from tkinter import Tk, Button, Entry, Label
from tkinter.messagebox import showerror
import math

canvas_width = 720
canvas_height = 300
points = []
a = ''
b = ''
c = ''

def put_point_from_entry(x, y):
    global points
    x1, y1 = int(x), int(y)
    points.append([int(x1), int(y1)])
    return [x1, y1]

def put_point_from_canvas(event):
    global points
    x1, y1, = event.x, event.y
    points.append([int(x1), int(y1)])
    create_figure('point', [x1, y1])
    

def create_figure(figure, points):
    global a, b, c
    color = "#476042"
    if figure == 'point':
        canv.create_oval(points[0] - 1, points[1] - 1, points[0] + 1, points[1] + 1, fill=color)

    elif figure == 'triangle':
        canv.delete(a)
        canv.delete(b)
        canv.delete(c)
        a = canv.create_line(points[0], points[1], fill=color)
        b = canv.create_line(points[0], points[2], fill=color)
        c = canv.create_line(points[2], points[1], fill=color)

def find_suitable_triangle():
    global points
    m_angle = -1
    m_sides = []
    side1 = 0
    side2 = 0
    side3 = 0
    l = len(points)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for z in range(j + 1, l):
                side1 = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** (1/2)
                side2 = ((points[i][0] - points[z][0]) ** 2 + (points[i][1] - points[z][1]) ** 2) ** (1/2)
                side3 = ((points[z][0] - points[j][0]) ** 2 + (points[z][1] - points[j][1]) ** 2) ** (1/2)
                angle = 0
                # print(side1, side2, side3)
                
                if side1 > side2 and side1 > side3:
                    # print((side2**2 + side3**2 - side1**2) / (2 * side2 * side3))
                    # print(side1)
                    angle = math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3))
                elif side2 > side1 and side2 > side3:
                    # print((side1**2 + side3**2 - side2**2) / (2 * side1 * side3))
                    # print(side2)
                    angle = math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3))
                elif side3 > side1 and side3 > side2:
                    # print((side2**2 + side1**2 - side3**2) / (2 * side2 * side1))
                    # print(side3)
                    angle = math.acos((side2**2 + side1**2 - side3**2) / (2 * side2 * side1))
                # print(math.degrees(angle))
                if math.degrees(angle) == 180: continue
                elif angle > m_angle:
                    m_angle = angle
                    m_sides = [points[i], points[j], points[z]]

    return m_sides

    
def data_check(key, x, y):
    global points
    if key == 'all':
        if x == None and y == None:
            return 'EXIT_SUCCESS'
        try:
            x = int(x)
            y = int(y)
        except:
            return 'WRONG_COORDINATES'
    elif key == 'quantity':
        if len(points) < 3:
            return 'WRONG_QUANTITY'

    return 'EXIT_SUCCESS'    

def show_error(text):
    showerror("Ошибка", text)

def on_button(key, x = None, y = None):
    global points
    if data_check('all', x, y) != 'EXIT_SUCCESS':
        show_error('Неправильные координаты')
        return None

    if key == 'enter x y':
        create_figure('point', put_point_from_entry(x, y))
    
    if data_check('qauntity', x, y) != 'EXIT_SUCCESS':
        show_error('Не хватает точек')
        return None

    if key == 'find triangle':
        m_sides = find_suitable_triangle()
        if  m_sides == []:
            show_error('Нет подходящих треугольников')
        else:
            create_figure('triangle', m_sides)
    
    if key == 'clear':
        canv.delete('all')
        points = []

window = Tk()

canv = Canvas(window,
        width=canvas_width,
        height=canvas_height,
        background="#777")

canv.bind("<Button-1>", put_point_from_canvas)

Label(text="Введите значение X (целые числа): ").grid(row=1, column=1)
Label(text="Введите значение Y (целые числа): ").grid(row=2, column=1)

x = StringVar()
y = StringVar()

x_value = Entry(window, width=30, textvariable=x).grid(row=1, column=2)
y_value = Entry(window, width=30, textvariable=y).grid(row=2, column=2)

Button(text='Поставить точку на холст', command=lambda: on_button('enter x y', x.get(), y.get())).grid(row=3, column=1)
Button(text='Найти треугольник', command=lambda: on_button('find triangle'), width=20).grid(row=4, column=1)
Button(text='Очистить холст', command=lambda: on_button('clear'), width=20).grid(row=5, column=1)


canv.grid(row=6, column=1, columnspan=2)

window.geometry('720x480')
window.mainloop()