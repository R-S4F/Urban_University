# Домашнее задание по теме "Оператор "with"".

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        unnecessary = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = dict()
        for _file in self.file_names:
            with open(str(_file), 'r+', encoding='utf-8') as file:
                _str = str(file.read()).lower()
                for un in unnecessary:
                    _str.replace(un, ' ')
                all_words[_file] = _str.split()
        return all_words

    def print_words_from(self, file_name):
        print(f'{file_name}: {self.get_all_words().get(file_name)}')

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.index(word.lower()) + 1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.count(word.lower()) + 1}


finder2 = WordsFinder('test.txt', 'test2.txt')
print(finder2.get_all_words())  # Все слова
finder2.print_words_from('test2.txt')
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
print(finder2.find('свинья'))
print(finder2.count('свинья'))
