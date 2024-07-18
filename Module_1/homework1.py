# 2023/09/21 00:00|Практическое задание по уроку "Строки и индексация строк"
# Работает как с четной длиной, так и с нечетной

example = "Urban"

print(example[0])

print(example[-1])

lenExample = len(example)
print(example[(lenExample // 2):lenExample])

print(example[::-1])

print(example[1::2])
