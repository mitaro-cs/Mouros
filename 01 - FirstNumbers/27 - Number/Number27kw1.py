clustersA = [[], []] # Создание двумерного массива для таблицы A

for line in open(r"01 - FirstNumbers\27 Number\27_A_17882.txt"): # Перебор каждой строки в списке
    x, y = [float(i) for i in line.split()] # Перевод каждого элемента в строке во Float 
    if y < 3:
        clustersA[0].append([x, y]) # Расформирование данных по масиву - 1 для массива A
    else:
        clustersA[1].append([x, y]) # Расформирование данных по масиву - 2 для массива A

clustersB = [[], [], []] # Создание трехмерного массива для таблицы B
for line in open(r"01 - FirstNumbers\27 Number\27_B_17882.txt"): # Перебор каждой строкит в списке
    x, y = [float(i) for i in line.split()] # Перевод каждого элемента в строке во Float
    if y < 3:
        clustersB[0].append([x, y]) # Расформирование данных по масиву - 1 для массива B
    elif x > 5:
        clustersB[1].append([x, y]) # Расформирование данных по масиву - 2 для массива B
    else:
        clustersB[2].append([x, y]) # Расформирование данных по масиву - 3 для массива B
def d(A, B): # Функция для нахождения расстояние между двумя точка ( формула даеться в условии задачи )
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 
def center(cl): # Функция для выявления центра
    m = []
    for p in cl: # Перебираем точки в кластере 
        sm = sum(d(p, p1) for p1 in cl) # Прощитыеваем сумму растояний от точки до всех других 
        m.append([sm, p]) # Добавляем минимальную сумму и точку которой соответвует сумм
    return min(m)[1] # Выводим только точку

centersA = [center(cl) for cl in clustersA] # Находим центральные точки каждого по отдельности 
centersB = [center(cl) for cl in clustersB] # Находим центральные точки каждого по отдельности
pxA = sum(x for x, y in centersA) / 2 * 10000 # Находим среднее арифметическое в кластере A # 2 Это колличесво кластеров
pyA = sum(y for x, y in centersA) / 2 * 10000 # В условии говориться что ответ нужно домножить на 10000
pxB = sum(x for x, y in centersB) / 3 * 10000 # Находим среднее арифметическое в кластере B
pyB = sum(y for x, y in centersB) / 3 * 10000 # В условии говориться что ответ нужно домножить на 10000
print(int(pxA), int(pyA))
print(int(pxB), int(pyB))