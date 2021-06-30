# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
import random
n = random.randint(1,10)
lst=[]
while len(lst)<n:
    lst.append(random.randint(-10,10))
summ=0
for el in lst:
    if el>0:
        summ+=el
print (lst)
print(summ)
