"""Продолжите программу, в которой нужно объявить функцию с именем check_phone и следующими параметрами (порядок следования важен):

phone - строка с номером телефона; только позиционные аргументы;
format_phone="8(xxx)xxx-xx-xx" - строка с проверяемым форматом номера телефона; только позиционные аргументы;
format_symbol='x' - форматный символ для произвольной цифры; принимает позиционные и именованные аргументы.
Функция check_phone должна проверять корректность записи номера телефона phone в соответствии с форматом, указанном в параметре format_phone. Формат телефонного номера format_phone содержит специальный символ (по умолчанию 'x'), который соответствует произвольной цифре от 0 до 9. Этот символ задается параметром format_symbol и изначально равен 'x'. Если номер телефона phone полностью соответствует заданному формату format_phone, то функция check_phone должна возвращать булево значение True, а иначе False.

Например:

res1 = check_phone("8(945)221-61-62") # True
res2 = check_phone("8(945)221-5007") # False
res3 = check_phone("+7(945)221-5007", "+7(xxx)xxx-xxxx") # True
res4 = check_phone('8(432)444-22-22', '8(xxx)xxx-xx-xx', format_symbol='*') # False
res5 = check_phone("+7(903)703-06-11", "+7(***)***-**-**", format_symbol='*') # True


Вызовите функцию check_phone для проверки следующего номера телефона:

phone_number = input()


на соответствие формата: +7(***)*** **** (параметр format_symbol='*'). Результат сохраните в переменной result.

P.S. На экран ничего выводить не нужно."""

def check_phone(phone, format_phone="8(xxx)xxx-xx-xx", /, format_symbol='x'):
    for i, c in enumerate(format_phone):
        if c == format_symbol:
            if not phone[i].isdigit():
                return False
        elif c != phone[i]:
            return False
    return True

phone_number = input()

check_phone(phone_number, "+7(***)*** ****", format_symbol='*')