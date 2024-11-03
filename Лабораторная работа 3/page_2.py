# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=","):
    # Разделяем строки по заданному разделителю и приводим к множествам
    set1 = set(group1.split(separator))
    set2 = set(group2.split(separator))

    # Находим пересечение двух множеств и сортируем результат
    common_participants = sorted(set1 & set2)

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
sep = '|'
result = find_common_participants(participants_first_group, participants_second_group, sep)
print(result)
# TODO Провеьте работу функции с разделителем отличным от запятой
