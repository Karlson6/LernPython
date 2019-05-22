# Функция, возращающая try, если введено целое число.
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Заставляем пользователя ввести целое число
user_age = input("Сколько Вам лет? (введите целое число): " )
while isInt(user_age) is False or int(user_age) < 0:
    user_age = input("Возраст не может быть отрицательной величиной. И не может быть прописан текстом. Попробуйте еще раз. Сколько Вам лет? (введите целое число): " )

# Заставляем пользователя ввести М/Ж 
gender = input("Ваш пол? (Введите букву М/Ж) : ")[:1]
while gender.lower() != "м" and gender.lower() != "ж":
    gender = input("Пол не определен. Попробуйте еще раз? (Введите букву М/Ж) : ")[:1] 

# Функция, определяющая, чем должен заниматься пользователь
def kind_of_activity(user_age, gender):
    if int(user_age) < 3:
        activity = "получать удовольствие от жизни"
    elif int(user_age) >= 3 and int(user_age) < 7:
        activity = "ходить в детский сад"
    elif int(user_age) >= 7 and int(user_age) < 18:
        activity = "учиться в школе"
    elif int(user_age) >= 18 and int(user_age) < 24:
        activity = "учиться в ВУЗе"
    elif (int(user_age) >= 24 and int(user_age) < 63 and gender.lower() == "ж") or (int(user_age) >= 24 and int(user_age) < 65 and gender.lower() == "м"):
        activity = "работать"
    else:
        activity = "пенсионерить"
    return activity

# Выводим результат деятельности пользователя
print(f'В вашем возрасте обычно люди предпочитают {kind_of_activity(user_age, gender)}')

