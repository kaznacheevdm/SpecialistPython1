# Дан список из элементов x = [-2,-1,0,1,2,3,4,5,6,7] - это координаты х, точек лежащих на прямой
# описываемой уравнением y=2x-4).
# Получить и вывести на экран список координат y для данного уравнения прямой.

# TODO: your code here
x = [-2,-1,0,1,2,3,4,5,6,7]
list_xy=[]
for i in x:
    list_xy.append([i,2*i-4])
print(list_xy)
