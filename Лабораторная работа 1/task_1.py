numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
a=numbers.index(None)
numbers[a]=(sum(numbers[0:a]) + sum(numbers[a+1:]))/len(numbers)
print("Измененный список:", numbers)
