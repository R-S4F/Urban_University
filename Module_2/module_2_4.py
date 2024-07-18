# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for k in range(2, i):
        if i % k == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime:
        primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)
