# Задание
# Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" и завершала работу при помощи оператора break
def ask_user():
    try:
        answer_d = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что расскажешь?": "Да не знаю. Делаю домашку по LernPython в 2 часа ночи", "Ладно, пока" : "Пока"}
        for score in answer_d:
            print(score)
            user_answer = input()
            if user_answer in answer_d:
                print(answer_d.get(user_answer))
    except KeyboardInterrupt:
        print("Как? Уже уходишь?... Ну пиши... Не забывай")
ask_user()

