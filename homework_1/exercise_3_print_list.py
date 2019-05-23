# Создаем список из 10-ти целых чисел
list10 = []
i = 0
x = 1
while i < 10:
    list10.append(x)
    x *= 2 
    i += 1
print(list10)

# Выводим на экран каждый элемент списка, увеличенный на 1
for score in list10:
    print(score + 1)