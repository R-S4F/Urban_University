from time import sleep


def is_exist(list_, string_, dict_key):
    checker = False
    for i in list_:
        if string_ == i.__dict__.get(dict_key):
            checker = True
            break

    return checker


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = int(hash(password))
        self.age = int(age)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        if videos is None:
            videos = []
        if users is None:
            users = []
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname != i.nickname:
                continue
            if hash(password) == i.password:
                self.current_user = i
                return
            else:
                break
        print('Вы ввели неверный логин или пароль')

    def register(self, nickname, password, age):
        nickname = str(nickname)
        if not is_exist(self.users, nickname, 'nickname'):
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")
            return

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for i in other:
            if not is_exist(self.videos, i.title, 'title'):
                self.videos.append(i)

    def get_videos(self, string_):
        list_ = list()
        for i in self.videos:
            if string_.upper() in i.title.upper():
                list_.append(i.title)
        return list_

    def watch_video(self, string_):
        current_video = None
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for i in self.videos:
            if string_ == i.title:
                current_video = i
                break

        if current_video is None:
            return

        if self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        if current_video.time_now > current_video.duration:
            current_video.time_now = 0

        for i in range(current_video.time_now + 1, current_video.duration + 1):
            print(i, end=' ')
            sleep(1)
        print("Конец видео")
