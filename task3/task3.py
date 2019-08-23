import sys
import re
# считывание данных из файлов и получение массива с данными по каждоый кассе
def cash_report(path):
    report = []
    for i in range(5):
        cash_temp = []
        cash_dict = {i: 0 for i in range(16)}
        temp_file = open(r'' + path + '\Cash' + str(i + 1) + '.txt', 'r')
        for item in temp_file:
            cash_temp.append(float(re.search(r'.+', item).group(0)))
        for i in range(len(cash_temp)):
            cash_dict[i] = cash_temp[i]
        report.append(cash_dict)
        temp_file.close()
    return report
# обработка данных и получение массива с максимальной нагрузкой и номер кассы
def max_report(report_by_day):
    day_max_all_cash_box = []
    cash_dict = {i: 0 for i in range(16)}
    # поиск максимума по одной кассе
    for i in range(len(report_by_day)):
        day_max = sorted(report_by_day[i].items(), key=lambda item: item[1])[-1]
        day_max_all_cash_box.append(day_max)
    # поиск максимума по всем кассам
    for i in range(len(report_by_day)):
        for j in range(len(report_by_day[i])):
            cash_dict[j] += report_by_day[i][j]
    over_all = sorted(cash_dict.items(), key=lambda item: -item[1])[0]
    return day_max_all_cash_box, over_all
# вызов функций и вывод информации на экран
def task3(path):
    report = max_report(cash_report(path))
    for i in range(len(report[0])):
        print('{}\n'.format(report[0][i][0] + 1))
    print('{}\n'.format(report[1][0]+1))

if __name__ == '__main__':
    if len (sys.argv) > 1:
        task3(sys.argv[1])