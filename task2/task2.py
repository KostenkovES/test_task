import sys
import re
# определение угла поворота вектора с концом в т.3 к вектору с концом в т.2
def rotate(point_1, point_2, point_3):
    return (point_2[0] - point_1[0]) * (point_3[1] - point_2[1]) - (point_2[1] - point_1[1]) * (point_3[0] - point_2[0])
# определение расположения точки относительно фигуры
def report(figure, point_to_check):
    if point_to_check in figure:
        return 'точка на одной из вершин'
    elif rotate(figure[0], figure[3], point_to_check) < 0 or rotate(figure[0], figure[1], point_to_check) > 0:
        return 'точка снаружи'
    elif rotate(figure[0], figure[1], point_to_check) == 0 or rotate(figure[1], figure[2], point_to_check) == 0 \
            or rotate(figure[2], figure[3], point_to_check) == 0 or rotate(figure[3], figure[0], point_to_check) == 0:
        return 'точка на одной из сторон'
    # точка находиться слева от вектора, соединяющего 1 и 3 вершину фигуры
    elif rotate(figure[0], figure[2], point_to_check) > 0:
        if rotate(figure[1], figure[2], point_to_check) > 0:
            return 'точка снаружи'
        elif rotate(figure[1], figure[2], point_to_check) < 0:
            return 'точка внутри'
    # точка находиться справа от вектора, соединяющего 1 и 3 вершину фигуры
    elif rotate(figure[0], figure[2], point_to_check) < 0:
        if rotate(figure[2], figure[3], point_to_check) > 0:
            return 'точка снаружи'
        elif rotate(figure[2], figure[3], point_to_check) < 0:
            return 'точка внутри'
# проверка на возможность преобразовать в float
def float_try_parse(string):
    try:
        return float(string), True
    except ValueError:
        return string, False
# получение данных и вывод на экран
def task2(file1, file2):
    figure, point_to_check = [],[]
    temp_file = open(r'' + file1 + '.txt', 'r')
    for item in temp_file:
        figure.append(re.split(r' ', re.search(r'.+', item).group(0)))
    temp_file.close()
    temp_file = open(r'' + file2 + '.txt', 'r')
    for item in temp_file:
        point_to_check.append(re.split(r' ', re.search(r'.+', item).group(0)))
    temp_file.close()
    for i in range(len(figure)):
        for j in range(len(figure[i])):
            if float_try_parse(figure[i][j])[1] == False:
                print('Координаты введены не корректно и не могут быть преобразованы в float')
                return False
            else:
                figure[i][j] = float_try_parse(figure[i][j])[0]
    if len(point_to_check) > 100:
        print('Количество точек больше 100')
        return False
    for i in range(len(point_to_check)):
        for j in range(len(point_to_check[i])):
            if float_try_parse(point_to_check[i][j])[1] == False:
                print('Координаты введены не корректно и не могут быть преобразованы в float')
                return False
            else:
                point_to_check[i][j] = float_try_parse(point_to_check[i][j])[0]
    for i in range(len(point_to_check)):
        print('{} - {}\n'.format(i, report(figure, point_to_check[i]), point_to_check[i]))
if __name__ == '__main__':
    if len (sys.argv) > 2:
        task2(sys.argv[1], sys.argv[2])