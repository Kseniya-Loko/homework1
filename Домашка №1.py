#x = input("Любое натуральное число, которое ты введешь, ряд арифметических операций превратит в 4. Введи число: ")
#print("Ваше число:", int(x))
#num_a = int(x * 2)
#print("Число", x,"умноженное на 2, равно", num_a)
#num_b = int(num_a + 8)
#print("Сумма числа", num_a,"и 8 равна числу", num_b)
#num_c = int(num_b / 2)
#print("Если число", num_b, "разделить на 2, получится число", num_c)
#num_d = num_c - int(x)
#print("Разница числа", num_c, "и числа", x,"равна числу", num_d)
#print("Финальный результат:", num_d)

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


#Любое натуральное число, которое ты введешь, ряд арифметических операций превратит в 4
#Введи число: (x)
#Операция n = x*2, вывести в тексте "Число x умноженное на 2 равно n"
#Операция f = n+8, вывести в тексте "Сумма n и 8 равна числу f"
#Операция g = f/2, вывести в тексте "Число f, разделенное на 2, равно числу g"
#Операция r = g - x, вывести в тексте "Разница числа g и числа x равна числу r"
#Финальный результат: r (= 4)


