import pygame

def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

# №1 Прямоугольник
def draw(surface, pos, color="white", borderFull=10, borderColor="black" , borderLeft=None, borderRight=None, borderTop=None, borderBottom=None, transparency=0):
    x1 = pos[0][0]
    x2 = pos[1][0]
    y1 = pos[0][1]
    y2 = pos[1][1]

    #Если пармаметтры не заполнены, то примут значение borderFull
    if borderLeft == None:
         borderLeft = borderFull
    if borderRight == None:
         borderRight = borderFull
    if borderTop == None:
         borderTop = borderFull
    if borderBottom == None:
         borderBottom = borderFull

    #Внутреняя область
    listBorder = [borderLeft, borderRight, borderTop, borderBottom, borderFull]
    min = borderFull
    summ = 0
    for i in listBorder:
        summ += i
        if i < min:
            min = i
    if not((x2-x1)/2>borderFull and (y2-y1)/2>borderFull):
        min = 0

    if not transparency:
        for x in range(x1+min, x2+1-min):
            for y in range(y1+min, y2+1-min):
                pixel(surface, color, (x, y))

    #Рамка
    if summ != 0 and (x2-x1)/2>borderFull and (y2-y1)/2>borderFull :
        draw(surface, [[x1,y1], [x2,y1+borderTop]], color=borderColor, borderFull=0)
        draw(surface, [[x2-borderRight,y1], [x2,y2]], color=borderColor, borderFull=0)
        draw(surface, [[x1,y2-borderBottom], [x2,y2]], color=borderColor, borderFull=0)
        draw(surface, [[x1,y1], [x1+borderLeft,y2]], color=borderColor, borderFull=0)
