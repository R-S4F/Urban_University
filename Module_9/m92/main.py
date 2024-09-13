# Домашнее задание по теме "Списковые, словарные сборки"
from pprint import pprint

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x)
                for x in first_strings
                if len(x) > 4]
second_result = [(a, b)
                 for a in first_strings
                 for b in second_strings
                 if len(a) == len(b)]
third_result = {a: len(a)
                for a in first_strings+second_strings
                if not len(a) % 2}

print(first_result)
pprint(second_result)
pprint(third_result)
