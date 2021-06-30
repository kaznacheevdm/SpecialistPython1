# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число: "))     # Первое число
second_number = int(input("Второе число: "))    # Второе число
list_num=[]
while first_number<second_number:
    if first_number%3==0:
        list_num.append(first_number)
    first_number+=1
print(list_num)
