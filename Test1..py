# 1st program
print(9**0.5*5) # возведение числа 9 в степень 0.5. и умножение на 5

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1) # boolean 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно

# 3rd program
print(2*2+2) # 2 умноженное на 2 плюс 2 без приоритета
print(2*(2+2)) # 2 умноженное на 2 плюс 2 с приоритетом для сложения.
print(6==8) # boolean результат сравнения этих двух выражений

# 4th program
# Вывести на экран первую цифру после запятой - 4.
print('123.456') # Дана строка '123.456'.
print(123.456*10) # строку преобразовать в число, Умножьте на 10 =1234.56
print(int(1234.56)) # далее использую оператор int для выведения целого числа из ранее полученного =1234
print(int(1234.56)/10) # полученное число делю на 10 с остатком =123.4
print(int(123.4)) # снова использую оператор int для выведения целого числа из полученного =123
print(int(((int(1234.56)/10)-(int(123.4)))*10))
'''в самом начале использую int, чтобы получить целое число после всех вычислений,
далее нахожу разницу полученных чисел (строки 17,18) и умножаю на 10.'''
