school_marks = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class':'4b', 'scores': [5,4,4,2,2,5,2,2]}]
i = 0
g_sum_class_marc = 0
g_count_class_marc = 0

# Считаем среднюю оценку по классу и по школе
for score1 in school_marks:
    sc_class = score1['school_class']
    avg_class_marc = sum(score1['scores']) / len(score1['scores'])
    g_sum_class_marc += sum(score1['scores'])
    g_count_class_marc += len(score1['scores'])
    print(f'Средняя оценка {sc_class} класса: {round(avg_class_marc,1)}')
print(f'Средняя оценка по школе: {round(g_sum_class_marc/g_count_class_marc,1)}')


    

