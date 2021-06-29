# Из остатков кирпичей Сергей сложил пирамиду.
# На вершине пирамиды лежит один кирпич, на втором сверху ряду два кирпича,
# на третьем - три, и т.д., в нижнем ряду пирамиды количество кирпичей равно количеству уровней пирамиды.
# После этого он написал на каждом кирпиче по числу, равному количеству кирпичей на этом уровне,
# т.е. на верхнем уровне 1, на втором уровне 2, и т.д. Определите сумму чисел написанных на кирпичах.
# Формат входных данных: Программе даётся целое число — количество уровней в пирамиде
# Формат выходных данных: Необходимо вывести сумму чисел написанных на кирпичах.

# TODO: your code here
floors = int(input("число этажей: "))
sum = 0
i=1
k=1

while i <= floors:
    j=1
    while j <= i:
        sum += k
        j += 1
        k += 1
    i += 1
print(sum)
