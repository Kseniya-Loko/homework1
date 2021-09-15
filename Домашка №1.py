print ( "Любое число, которое ты введешь, ряд арифметических действий превратит в 4")
print ("Введи число")
num_in = input()
num_a = int(num_in)
num_b = num_a * 2
num_c = num_b + 8
num_d = int(num_c/2)
num_f = num_d - num_a
print("Число", num_a,"умноженное на 2, равно", num_b)
print("Сумма числа", num_b,"и 8 равна числу", num_c)
print("Если число", num_c, "разделить на 2, получится число", num_d)
print("Разница числа", num_d, "и числа", num_a,"равна числу", num_f)
print("Финальный результат:", num_f)
