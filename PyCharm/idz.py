#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
поезда; время отправления. Написать программу, выполняющую следующие действия:
ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
быть упорядочены по номерам поездов;
вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
выдать на дисплей соответствующее сообщение.
"""

import sys


def add(trains, name, num, time):
    train = {
        'name': name,
        'num': num,
        'time': time,
    }

    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('num', ''))


def listt(trains):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for idx, train in enumerate(trains, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('name', ''),
                train.get('num', ''),
                train.get('time', 0)
            )
        )

    print(line)


def select_train(trains, number):
    """""
    Выбрать работников с заданным стажем
    """""
    # Сформировать список поездов
    result = []
    for rattler in trains:
        if rattler.get('num') == number:
            result.append(rattler)

    # Возвратить список выбранных работников
    return result


def main():
    route = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            add(route, name, num, time)

        elif command == 'list':
            listt(route)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            number = int(parts[1])
            selected = select_train(route, number)
            listt(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
