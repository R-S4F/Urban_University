# Домашнее задание по теме "Многопроцессное программирование"
import datetime
import multiprocessing


def read_info(name):
    print(name)
    all_data = list()
    with open(str(name), 'r') as file:
        while True:
            x = file.readline()
            if x == '':
                break
            all_data.append(x)


names_list = [f'file {x+1}.txt' for x in range(4)]

# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, names_list)
#     end = datetime.datetime.now()
#     print(end - start)

if __name__ == '__main__':
    start = datetime.datetime.now()
    for name in names_list:
        read_info(name)
    end = datetime.datetime.now()
    print(end - start)
