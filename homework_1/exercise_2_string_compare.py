# Функция, которая сравнивает входящие переменные
def string_compare(string1, string2):
    if type(string1) is not str or type(string2) is not str:
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3
    else:
        return 'Сегодня твой день. Ты поймал исключение'

while 1 == 1:
    st1 = input('Введите первую строку :')
    st2 = input('Введите вторую строку :')
    print(string_compare(st1, st2))
