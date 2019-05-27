# Задание
# Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
# Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало


def get_summ(num_one, num_two):
    try:
        u_summ = int(num_one) + int(num_two)
        print(u_summ)
    except ValueError:
        print("Я питаюсь только числами. А ты решил обмануть меня? Подсунул не число?")

while True:
    user_num_one = input("Введи число: ") 
    user_num_two = input("Введи еще одно число: ") 

    get_summ(user_num_one, user_num_two)





    
    
