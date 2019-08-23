import sys
import re
# преобразуем данные из файла в массив с значениями типа int
def time_report_list(file_name):
    report = []
    temp_file = open(r'' + file_name + '.txt', 'r')
    for item in temp_file:
        report.append(re.split(r' ', re.search(r'\d+:\d\d \d+:\d\d', item).group(0)))
    temp_file.close()
    for i in range(len(report)):
        for j in range(len(report[i])):
            report[i][j] = int(report[i][j].replace(':', ''))
    for i in report:
        if i[1] < i[0]:
            print('Посетитель ушел раньше, чем пришел!')
            return False
    return report
# получаем массив диапазонов с максимальной посещаемостью
def most_visitors(report):
    if report == False:
        return False
    # массив с количеством посетителей в каждую минуту работы магазина
    stats_by_minute = [[[0] for j in range(60)] for i in range(12)]
    busiest_time, temp_max, time_ranges = [], [], []
    # поминутный анализ присутствия в маназине каждого клиента
    for i in range(len(report)):
        hours_start = report[i][0] // 100
        hours_stop = report[i][1] // 100
        minutes = report[i][0] % 100
        interval = report[i][1] - report[i][0]
        if hours_stop - hours_start > 0:
            interval -= (hours_stop - hours_start) * 40
        while hours_start <= hours_stop and interval > 0:
            while interval > 0:
                if minutes == 60:
                    hours_start += 1
                    minutes = 0
                    break
                stats_by_minute[hours_start - 8][minutes][0] += 1
                interval -= 1
                minutes += 1
    # максимальное количество посетителей каждый час
    for item in stats_by_minute:
        temp_max.append(max(item))
    # все минуты с максимальным количеством посетителей
    for i in range(len(stats_by_minute)):
        for j in range(len(stats_by_minute[i])):
            if stats_by_minute[i][j] == max(temp_max):
                busiest_time.append((8 + i) * 100 + j)
    # интервалы с максимальный количеством посетителей
    time_ranges.append(busiest_time[0])
    for i in range(len(busiest_time) - 1):
        if busiest_time[i] != busiest_time[i + 1] - 1:
            time_ranges.append(busiest_time[i])
            time_ranges.append(busiest_time[i + 1])
        if i + 1 == len(busiest_time) - 1:
            time_ranges.append(busiest_time[i + 1])
    # чистка интервалов от "перескакивания через час" и подготовка в выводному формату
    mark_1, mark_2 = 0, len(time_ranges) - 1
    # mark_2 = len(time_ranges)-1
    while mark_1 < mark_2:
        if time_ranges[mark_1] == time_ranges[mark_1 + 1] - 41:
            time_ranges.pop(mark_1)
            time_ranges.pop(mark_1)
            mark_2 -= 2
        mark_1 += 1
    for i in range(len(time_ranges)):
        if time_ranges[i] % 100 == 59:
            time_ranges[i] += 41
        elif time_ranges[i] % 10 == 9:
            time_ranges[i] += 1
    return time_ranges
# вызов требуемых методов и вывод на экран
def task4(file_name):
    ranges = most_visitors(time_report_list(file_name))
    if ranges == False:
        return False
    for i in range(len(ranges) // 2):
        print('{}:{:02d} {}:{:02d}\n'.format(ranges[i * 2] // 100, ranges[i * 2] % 100, ranges[i * 2 + 1] // 100,
                                             ranges[i * 2 + 1] % 100))

if __name__ == '__main__':
    if len (sys.argv) > 1:
        task4(sys.argv[1])