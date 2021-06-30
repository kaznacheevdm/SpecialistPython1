# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

max_el=tup[0]
for t in tup:
    if t>max_el:
        max_el=t
print(max_el)
