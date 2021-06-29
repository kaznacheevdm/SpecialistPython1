# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
unit = int(input("введите число: "))
if not unit%3 and not unit%5:
    print("FooBar")
elif not unit%3:
    print("Foo")
elif not unit%5:
    print("Bar")
