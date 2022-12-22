#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math
import sys


def cylinder():
    """""
    Вычисление площади цилиндра
    """""
    r = int(input("Введите радиус: "))
    h = int(input("Введите высоту: "))
    while True:
        command = int(input("Выбирете варинат:\n"
                            "1: площадь боковой поверхности цилиндра\n"
                            "2: площадь цилиндра\n"))
        if command == 1:
            s = 2 * math.pi * r * h
            print("S(боковая) = ", s)
            break
        elif command == 2:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print("S(полная) = ", s)
            break

        else:
            print(f"Неизвестная комманда {command}", file=sys.stderr)
            break


def circle(r):
    """""
    Вычисление площади круга в цилиндре
    """""
    return math.pi * (r ** 2)


def main():
    """""
    Главная функция программы
    """""
    cylinder()


if __name__ == '__main__':
    main()
