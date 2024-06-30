#Задание 1 
#Напишите функцию fib(), которая будет генерировать числа в последовательности Фибоначчи и принимать в качестве аргумента целое число, обозначающее номер числа в последовательности, на котором следует остановиться.
def fib(n):
a, b = 0, 1
result = []
while len(result) < n:
result.append(a)
a, b = b, a + b
return result

#Задание  «со  звёздочкой»  (повышенной  сложности):  сделайте  функцию-генератор,используя  yield.
def fib(n):
a, b = 0, 1
for _ in range(n):
yield a
a, b = b, a + b
