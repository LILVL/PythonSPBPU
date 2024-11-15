numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
a = 0
b=0
for i in range(len(numbers)):
    if(numbers[i] is None):
        a = i
    else:
        b+=numbers[i]
numbers[a] = (b/(len(numbers)))
print("Измененный список:", numbers)
#Программа рассчитана на один "None" в массиве типа integer любой длины
