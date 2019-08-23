import sys
import re
# вычисления квантилей (для медианы и 90 перцентиль)
def quantile(value: float, data):
    return data[int(value * (len(data) - 1))] + \
           (value * (len(data) - 1) + 1 - int(value * (len(data) - 1) + 1)) * \
           (data[int(value * (len(data) - 1) + 1)] - data[int(value * (len(data) - 1))])
# получение требуемых результатов в виде массива (списка)
def result(path):
    data, result = [], []
    file = open(r'' + path + '.txt', 'r')
    for item in file:
        data.append(float(re.search(r'.+', item).group(0)))
    file.close()
    if len(data) > 1000:
        print('Количество чисел больше 1000')
        return False
    for i in data:
        if i < -32768 or i > 32767:
            print('Числа не находятся в диапазон от -32 768 до 32 767')
            return False
    data.sort()
    result.append(quantile(0.9, data))
    result.append(quantile(0.5, data))
    result.append(data[-1])
    result.append(data[0])
    result.append(float(sum(data)) / len(data))
    return result
# вывод на жкран консоли в требуемом формате
def task1(path):
    to_print = result(path)
    if to_print == False:
        return False
    for i in to_print:
        print("{:.2f}\n".format(i))

if __name__ == '__main__':
    if len (sys.argv) > 1:
        task1(sys.argv[1])