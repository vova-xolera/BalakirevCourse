"""Продолжите программу, в которой нужно объявить функцию с именем is_right_rect и следующими параметрами (порядок следования важен):

a, b, c, d - координаты четырехугольника на плоскости; только позиционные аргументы;
precision=0.001 - точность соответствия четырехугольника прямоугольнику; только именованные аргументы.
Функция is_right_rect должна по переданным координатам a, b, c, d четырехугольника определить, что это прямоугольник. Если это так, то возвращается булево значение True, а иначе False.

Например, для следующего четырехугольника:


вызов функции is_right_rect должен давать True:

result = is_right_rect((3, 1), (6, 7), (10, 5), (7, -1))


Для реализации такой проверки удобно воспользоваться следующим свойством скалярного произведения радиус-векторов:



Вызовите функцию is_right_rect для следующих координат четырехугольника (координаты идут по порядку друг за другом):

rect_coords = [(float(x.split('=')[0]), float(x.split('=')[1])) for x in input().split()]


Здесь список rect_coords имеет формат:

rect_coords = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]

Результат работы функции is_right_rect сохраните в переменной result.

При реализации функции is_right_rect следует использовать только текущие знания без применения каких-либо внешних библиотек.

P.S. На экран ничего выводить не нужно."""

def is_right_rect(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float], d: tuple[float, float], /, *, precision=0.001):
    coords = [a, b, c, d]
    for i, p in enumerate(coords):
        other_coords = coords.copy()
        for_corner = i + 1 if i < 2 else i - 2
        other_coords.pop(i)
        other_coords.pop(for_corner)
        x0 = - p[0] + other_coords[0][0]
        y0 = - p[1] + other_coords[0][1]
        x1 = - p[0] + other_coords[1][0]
        y1 = - p[1] + other_coords[1][1]
        cos_p = (x0 * x1 + y0 * y1) / (((x0 ** 2 + y0 ** 2) ** 0.5) * ((x1 ** 2 + y1 ** 2) ** 0.5))
        if abs(cos_p) >= precision:
            return False
    return True

print(is_right_rect((3, 1), (6, 7), (10, 5), (7, -1)))
print(is_right_rect((3, 1), (6, 7), (10, 5), (7, -10)))