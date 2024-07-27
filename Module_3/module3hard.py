def calculate_structure_sum(n):
    summ = 0
    for i in n:
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            for k in i.items():
                summ += calculate_structure_sum(k)
        else:
            summ += calculate_structure_sum(i)
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
