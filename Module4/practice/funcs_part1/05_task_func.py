# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def can_triangle(p1, p2, p3):
    line_a=distance(*p1,*p2)
    line_b=distance(*p2,*p3)
    line_c=distance(*p1,*p3)

    if line_a<line_b+line_c:
        if line_b<line_a+line_c:
            if line_c<line_b+line_a:
                return True
    return False

def perimetr(p1, p2, p3):
    return distance(*p1,*p2)+distance(*p2,*p3)+distance(*p1,*p3)
 
def square(p1,p2,p3):
    per=perimetr(p1,p2,p3)
    line_a=distance(*p1,*p2)
    line_b=distance(*p2,*p3)
    line_c=distance(*p1,*p3)
    return (per*(per-line_a)*(per-line_b)*(per-line_c))**0.5

# Пример вызова функции
pic=(10, 12), (14, 18), (12, 12)
if (can_triangle(*pic)):
    print(perimetr(*pic))
    print(square(*pic))
else:
    print("It's no a triangle")


# Не забудьте протестировать вашу функцию
