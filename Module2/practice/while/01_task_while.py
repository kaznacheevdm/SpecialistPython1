# Даны два целые числа a и b. Выведите на экран все целые четные числа от a до b включительно.
# Формат входных данных: Дано два целых числа a и b. Гарантируется, что a < b
# Формат выходных данных: Выведите все числа, требуемые по условию задачи.

# TODO: your code here
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while a <= b:
    if a%2 == 0:
        print(a)
    a+=1
