# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def can_triangle(p1, p2, p3):
    p1x, p1y=p1
    p2x, p2y=p2
    p3x, p3y=p3

    if distance(p1x,p1y,p2x,p2y)<distance(p3x,p3y,p2x,p2y)+distance(p1x,p1y,p3x,p3y):
        if distance(p3x,p3y,p2x,p2y)<distance(p1x,p1y,p2x,p2y)+distance(p1x,p1y,p3x,p3y):
            if distance(p1x,p1y,p3x,p3y)<distance(p3x,p3y,p2x,p2y)+distance(p1x,p1y,p2x,p2y):
                return True
    return False
# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))

# Не забудьте протестировать вашу функцию
