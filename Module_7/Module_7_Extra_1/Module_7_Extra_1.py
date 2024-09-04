# Домашнее задание по теме "Форматирование строк".
##################################################
# Использование %: Строки 88-111
# Использование format(): Строки 117-132
# Использование f-строки: Строки 134-182
##################################################

class Team:
    def __init__(self, name='None', count=0):
        self.__name = str(name)
        self.__count = int(count)
        self.__time = None
        self.__score = None

    def get_name(self):
        return self.__name

    def get_count(self):
        return self.__count

    def get_time(self):
        return self.__time

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_count(self, count):
        self.__count = count

    def set_time(self, time):
        self.__time = time

    def set_score(self, score):
        self.__score = score


class Challenge:
    def __init__(self, *args):
        self.team_list = list(args)

    def get_teams(self):
        for i in self.team_list:
            print(f'Номер команды "{i.get_name()}" : {self.team_list.index(i) + 1} !')

    @staticmethod
    def member(count):
        _tuple = (2, 3, 4)
        if count % 10 == 1 and count != 11:
            return 'участник'
        elif count % 10 in _tuple and count not in range(12, 15):
            return 'участника'
        else:
            return 'участников'

    @staticmethod
    def point(score):
        _tuple = (2, 3, 4)
        if score % 10 == 1 and score != 11:
            return 'задачу'
        elif score % 10 in _tuple and score not in range(12, 15):
            return 'задачи'
        else:
            return 'задач'

    @staticmethod
    def insertion_sort(ls, ind):
        for i in range(1, len(ls)):
            key = ls[i]
            j = i - 1
            while ls[j][ind] > key[ind] and j >= 0:
                ls[j + 1] = ls[j]
                j -= 1
            ls[j + 1] = key
        return ls[::-1]

    def remove_losers(self, ls, ind=1):
        ls = self.insertion_sort(ls, ind)
        if ls[-1][ind] != ls[0][ind]:
            ls.pop(-1)
            return self.remove_losers(ls, ind)
        if len(ls) > 1 and ls[0][2] != ls[1][2]:
            ls = self.remove_losers(ls, 2)
        return ls

    def print_team_count(self, index):
        if isinstance(index, int) and index > 0:
            index -= 1
        else:
            return
        name = self.team_list[index].get_name()
        count = self.team_list[index].get_count()
        mem = self.member(count)
        str1 = 'В команде "%s" %s %s!' % (name, count, mem)
        print(str1)

    def print_all_teams_count(self):
        _list = list()
        _str = str()
        for i in self.team_list:
            _list.append(i.get_count())
        for i in _list:
            if _list.index(i) == 0:
                _str = '%s' % i
            elif _list.index(i) == _list.__len__() - 1:
                _str += ' и %s %s!' % (i, self.member(i))
            else:
                _str += ', %s' % i
        print('Итого в командах %s' % _str)

    def print_team_score(self, index):
        if isinstance(index, int) and index > 0:
            index -= 1
        else:
            return
        name = self.team_list[index].get_name()
        score = self.team_list[index].get_score()
        mem = self.point(score)
        str1 = 'Команда "{name}" решила {score} {mem}!'.format(name=name, score=score, mem=mem)
        print(str1)

    def print_team_time(self, index):
        if isinstance(index, int) and index > 0:
            index -= 1
        else:
            return
        name = self.team_list[index].get_name()
        time = self.team_list[index].get_time()
        str1 = '"{name}" решили задачи за {time} секунд!'.format(name=name, time=time)
        print(str1)

    def print_all_score(self):
        __list = list()
        _str = str()
        k = 0
        for i in self.team_list:
            __list.append(i.get_score())
        for i in __list:
            if __list.index(i) == 0:
                _str = f'{i}'
                k += 1
            elif k == len(__list) - 1:
                _str += f' и {i} {self.point(i)}!'
            else:
                _str += f', {i}'
                k += 1
        print(f'Команды решили {_str}')

    def print_results(self):
        _list = list()
        _str = str()
        for i in self.team_list:
            _list.append((i.get_name(), i.get_score(), i.get_time()))
        _list = self.remove_losers(_list)
        if len(_list) > 1:
            for i in _list:
                _list[_list.index(i)] = i[0]
            for i in _list:
                if _list.index(i) == 0:
                    _str = f'"{i}"'
                elif _list.index(i) == _list.__len__() - 1:
                    _str += f' и "{i}"'
                else:
                    _str += f', "{i}"'
            print(f'У команд {_str} ничья!')
        else:
            print(f'Команда "{_list[0][0]}" - победитель!')

    def print_total_info(self):
        score_total = list()
        time_total = list()
        for i in self.team_list:
            time_total.append(i.get_time())
            score_total.append(i.get_score())

        score_total = sum(score_total)
        time_avg = sum(time_total) / score_total
        _str = (f'Сегодня было решено {score_total} {self.point(score_total)}, '
                f'в среднем по {time_avg} секунды на задачу!')
        print(_str)


teams = list()
teams.append(Team('Мастера кода', 5))
teams.append(Team('Волшебники данных', 6))
teams.append(Team('Дровосеки', 22))
challenge1 = Challenge(*teams)

challenge1.get_teams()
print('\n')

teams[0].set_score(32)
teams[1].set_score(42)
teams[2].set_score(42)

#Можно и так
#challenge1.team_list[0].set_score(32)
#challenge1.team_list[1].set_score(42)
#challenge1.team_list[2].set_score(42)

teams[0].set_time(1552.512)
teams[1].set_time(2153.31451)
teams[2].set_time(3123.31451)

challenge1.print_team_count(1)
challenge1.print_team_count(2)
challenge1.print_team_count(3)
print('\n')

challenge1.print_team_score(1)
challenge1.print_team_score(2)
challenge1.print_team_score(3)
print('\n')

challenge1.print_team_time(1)
challenge1.print_team_time(2)
challenge1.print_team_time(3)
print('\n')

challenge1.print_all_teams_count()
challenge1.print_all_score()
challenge1.print_results()
challenge1.print_total_info()
