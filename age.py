def grading_of_age(age):
    if age.isnumeric():
        age = int(age)
        if age < 7 :
            return 'Пользователь посещает детский сад'
        elif age >= 7 and age <=18:
            return 'Пользователь учится в школе'
        elif age > 18 and age <= 22:
            return 'Пользователь учится в ВУЗе'
        elif age > 22 and age < 100:
            return 'Пользователь работает'
    return 'Пользователь ввел некорректное значение'

age = input('Введите возраст:')
result = grading_of_age(age)
print(result)