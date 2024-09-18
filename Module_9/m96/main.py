# Домашнее задание по теме "Генераторы"

def all_variants(text):
    __len = len(text) + 1
    for __i in range(1, __len):
        for __k in range(0, __len - __i):
            yield text[__k:__k + __i]


a = all_variants("abcdefghijklmnopqrstuvwxyz")
for i in a:
    print(i)