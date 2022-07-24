import json
import numpy as np
import matplotlib.pyplot as plt
import sys

markers = ['o', 'v', '^', '<', '>', '1', 's', 'p', 'P', '*', '+', 'x', 'D', '|', 'X']

def build_piecewise_plot_function(opts, counters, min_size, max_size, step, l, legends):
    global markers
    t = 0
    sizes = 0

    for opt in opts:
        for counter in counters:
        
            x = []
            y = []
            for NMAX in range(min_size, max_size + 1, step):
                with open(f"./preproc/{opt}_0{counter}_{NMAX}.json") as file:
                    data = json.load(file)
                    x.append(int(data['NMAX']))
                    y.append(int(data['mean']))
                    if NMAX % (step * 10) == 0:
                        sizes += 1
            plt.plot(x, y, markers[t], linewidth=1, markevery=5, ls='-', label=legends[t])
            t += 1
    plt.locator_params(axis="x", nbins = sizes // 10)
    plt.legend()
    plt.savefig('./graphs/graph_01.svg')
    plt.clf()

def build_piecewise_linear_plot_with_error(opt, counters, min_size, max_size, step, line_type):  
    t = 0
    sizes = 0

    for counter in counters:
        x = []
        y = []
        yerr = [[], []]

        for NMAX in range(min_size, max_size + 1, step):
            with open(f"./preproc/{opt}_0{counter}_{NMAX}.json") as file:
                data = json.load(file)
                x.append(int(data['NMAX']))
                y.append(int(data['median']))
                yerr[0].append(int(data['median']) - int(data['minimum']))
                yerr[1].append(int(data['maximum']) - int(data['median']))
                if NMAX % (step * 10) == 0:
                    sizes += 1
        plt.errorbar(x, y, yerr=yerr, ls=line_type[t%3], label=f'0{counter}_{opt}')
        t += 1

    plt.locator_params(axis="x", nbins = sizes // 2)
    plt.legend()
    plt.savefig('./graphs/graph_02.svg')

def build_box_plot(opt, counters, min_size, max_size, step):
    x = []
    sizes = []

    for NMAX in range(min_size, max_size + 1, step):
        with open(f"./data/{opt}_03_{NMAX}.txt") as file:
            data = list(map(int, file.read().split()))
            x.append(data)
            sizes.append(NMAX)

    plt.boxplot(x, showfliers=False)
    plt.xticks(list(range(1, len(sizes) + 1)), sizes)
    plt.locator_params(axis="x", nbins = len(sizes) // 9)
    plt.legend(['01_O3'])
    plt.savefig('./graphs/graph_03.svg')

opts = ("O1", "O2", "O3", "O0", "Os")
counters = (1, 2, 3)
max_size = int(str(sys.argv[2]))
min_size = int(str(sys.argv[1]))
step = int(sys.argv[3])
l = len(opts) * len(counters)

print("Создание графика [0 / 3]", end='\r')

legends = ('O1_01', 'O1_02', 'O1_03',\
            'O2_01', 'O2_02', 'O2_03',\
            'O3_01', 'O3_02', 'O3_03',\
            'O0_01', 'O0_02', 'O0_03',\
            'Os_01', 'Os_02', 'Os_03',)
plt.figure(figsize=(16, 9))
plt.grid(True)
plt.xlabel("Количество элементов")
plt.ylabel("Время, мкс")
plt.title("Кусочно линейный график")
build_piecewise_plot_function(opts, counters, min_size, max_size, step, l, legends)

print("Создание графика [1 / 3]", end='\r')

plt.figure(figsize=(16, 9))
plt.grid(True)
plt.xlabel("Количество элементов")
plt.ylabel("Время, мкс")
plt.title("Кусочно линейный график с ошибками")
build_piecewise_linear_plot_with_error('O2', counters, min_size, max_size, step, line_type=['-', ':', '--'])

print("Создание графика [2 / 3]", end='\r')

plt.figure(figsize=(16, 9))
plt.grid(True)
plt.xlabel("Количество элементов")
plt.ylabel("Время, мкс")
plt.title("График с усами")
build_box_plot('O3', counters, min_size, max_size, step)

print("Создание графика [3 / 3]", end='\n')
