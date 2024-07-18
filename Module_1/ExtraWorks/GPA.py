# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students) # Создаю список из множества,
students.sort()           # чтобы отсортировать этот список

students_dict = dict()
print(students_dict)

i = 0 # Просто переменная для copy-paste

###########################################################
students_dict[students[i]] = sum(grades[i]) / len(grades[i])
i = i + 1
students_dict[students[i]] = sum(grades[i]) / len(grades[i])
i = i + 1
students_dict[students[i]] = sum(grades[i]) / len(grades[i])
i = i + 1
students_dict[students[i]] = sum(grades[i]) / len(grades[i])
i = i + 1
students_dict[students[i]] = sum(grades[i]) / len(grades[i])
i = i + 1
############################################################
print(students_dict)