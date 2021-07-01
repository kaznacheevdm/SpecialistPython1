# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    new_number=number
    revs_num = 0
    while new_number//10>0:
        revs_num = revs_num*10+new_number%10
        new_number=new_number//10
    revs_num = revs_num*10+new_number%10
    if number!=revs_num:
        return "no"
    return "yes"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
