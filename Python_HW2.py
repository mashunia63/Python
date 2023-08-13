import math

print("1. Создать переменную item_1 типа integer.")
item_1 = 2

print("2. Создать переменную item_2 типа integer.")
item_2 = 4

print("item_1 = ", item_1)
print("item_2 = ", item_2)

print("3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.")
result_sum = item_1 + item_2
print(result_sum)

print("5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.")
if item_1 > item_2 : result_subtr = item_2 - item_1
result_subtr = item_1 - item_2

print(result_subtr)

print("7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.")
result_multi = item_1 * item_2
print(result_multi)

print("9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.")
result_exp = item_1**item_2
print(result_exp)

print("11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.")
result_m_exp = math.pow(item_1,item_2)
print(result_m_exp)

print("13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item.")
result_s_root = item_1 ** (0.5)
print(result_s_root)

print("15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.")
result_m_s_root = math.sqrt(item_1)
print(result_m_s_root)

print("17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.")
result_mp_s_root = math.pow(item_2,0.5)
print(result_mp_s_root)

print("19. Присвоить переменной item_1 odd значение - нечетное")
item_1 = 5
print("item_1 = ",item_1)

print("Присвоить переменной item_2 even значение - четное")
item_2 = 3
print("item_2 = ",item_2)

print("21. Создать переменную result_division в которой вы разделите item_1 на item_2.")
result_division = item_1/item_2
print(result_division)

print("23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.")
result_m_floor = math.floor(result_division)
print(result_m_floor)

print("25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.")
#result_m_ceil = math.ceil(result_division)
result_m_ceil = round(result_division)
print(result_m_ceil)

print("27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.")
result_int = int(result_division)
print(result_int)

print(" 29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.")
result_no_division_loss = item_1//item_2
print(result_no_division_loss)

print("31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.")
result_division_loss = item_1%item_2
print(result_division_loss)

item_3 = 15
print(item_3)

print("Прибавить 10 к item_3 с присвоением.")
item_3 += 10
print (item_3)

print ("Отнять 5 от item_3 с присвоением.")
item_3 -= 5
print(item_3)

print("38. Умножить item_3 на 3 с присвоением.")
item_3 *= 3
print(item_3)

print("40. Разделить item_3 на 2 с присвоением.")
item_3 /= 2
print(item_3)

print("42. Возвести в степень 2 item_3 с присвоением.")
item_3 **= 2
print(item_3)

print("44. Найти квадратный корень item_3 с присвоением.")
item_3 = math.sqrt(item_3)
print(item_3)

print("46. Присвоить остаток от деления item_3")
item_3 = item_3 % 3
print(item_3)

print("48. Создать переменную b_item_t и присвоить True")
b_item_t = True
print(" 49. Создать переменную b_item_f и присвоить False")
b_item_f = False

print("50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f")
b_item_relult_sum = b_item_f + b_item_t
print(b_item_relult_sum)

print("52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f")
b_item_relult_subtr =  b_item_t - b_item_f
print(b_item_relult_subtr)

print("54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f")
b_item_relult_multi = b_item_f * b_item_t
print(b_item_relult_multi)

print("56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f")
#деление на 0
# b_item_relult_division = b_item_t / b_item_f
#print(b_item_relult_division)
print("ошибка")

print("58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int ")
b_item_1_int = int(b_item_t)
print(b_item_1_int)

print("60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int")
b_item_2_int = int (b_item_f)
print(b_item_2_int)
