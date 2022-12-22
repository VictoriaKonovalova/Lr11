#!/usr/bin/evn python3
# -*- config: utf-8 -*-
"""
Решите следующую задачу: напишите программу, в которой определены следующие четыре
функции:
1. Функция getInput() не имеет параметров, запрашивает ввод с клавиатуры и возвращает
в основную программу полученную строку.
2. Функция testInput() имеет один параметр. В теле она проверяет, можно ли переданное
ей значение преобразовать к целому числу. Если можно, возвращает логическое True.
Если нельзя – False.
3. Функция strToInt() имеет один параметр. В теле преобразовывает переданное значение
к целочисленному типу. Возвращает полученное число.
4. Функция printInt() имеет один параметр. Она выводит переданное значение на экран и
ничего не возвращает.
В основной ветке программы вызовите первую функцию. То, что она вернула, передайте во
вторую функцию. Если вторая функция вернула True, то те же данные (из первой функции)
передайте в третью функцию, а возвращенное третьей функцией значение – в четвертую.
"""


def get_input():
    a = input('Enter:')
    return a


def test_input(a):
    return a.isdigit()


def str_to_int(a):
    i = int(a)
    return i


def print_int(i):
    print(i)


if __name__ == '__main__':
    s = get_input()
    if test_input(s):
        print_int(str_to_int(s))