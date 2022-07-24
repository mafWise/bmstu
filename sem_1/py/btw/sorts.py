# Сортировка вставками



import re, random

# Сортировка вставками
def sort1():
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor

# Сортировка выбором
def sort2():
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    
# Сортировка Шелла?
def sort3():
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

# Сортировка пузьрком
def sort4():
    l = len(arr)
    for i in range(l-1):
        for j in range(l-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Сортировка пузырьком с флагом
def sort5():
    l = len(arr)
    for i in range(l-1):
        sort = True
        for j in range(l-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sort = False
        if sort:
            break

# Сортировка шейкером
def sort6():
    l = len(arr)
    sort = False
    a = 0
    b = 0
    while not sort:
        sort = True
        for j in range(b, l-a-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sort = False
    
        if sort:
            break
        for i in range(l-a-1, b,-1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        a += 1
        b += 1

# Вставка с барьером
def sort7(arr):
    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[0] = arr[i]
        j = i - 1
        while (arr[0] < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = arr[0]
    return arr

# Метод Шелла?
def sort8():
    inc = len(arr)//2
    while inc:
        for i,el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5 // 11)
            
# Быстрая сортировка
def sort9(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    m = []
    M = []
    eq = []
    for i in nums:
        if i < q:
            m.append(i)
        elif i > q:
            M.append(i)
        else:
            eq.append(i)
    return sort9(m) + eq + sort9(M)
    
# Сортировка вставками с бинарным поиском

	
def sort10(data):
    for i in range(1, len(data) - 1):
        key = data[i]
        lo, hi = 0, i - 1
        while lo < hi:
            mid = (hi + lo) // 2
            print(mid, key, lo, hi)
            if key < data[mid]:
                hi = mid - 1
            elif key > data[mid]:
                lo = mid + 1
        for j in range(i, lo + 1, -1):
            data[j + 1] = data[j]
        data[lo] = key
    return data



arr = [5,2,1,8,6,3,4,5,213,2142,1567]
# sort10()
print(arr)

print(sort10(arr))

#print(sort7(arr)[1:])
