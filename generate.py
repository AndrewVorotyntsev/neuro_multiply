import csv
import random


a = 5


# 1 Функция для порождающего объекта
def multiply(x1, x2, x3):
    return a * (x1 * x2 * x3)


# Создание обучающей выборки
with open("data_mul_1.csv", encoding='utf-8', mode="w") as data_mul_1:
    data_mul_1.seek(0)
    names = ["x1", "x2", "x3", "y"]
    # Создаем объект reader, указываем символ-разделитель ","
    file_writer = csv.DictWriter(data_mul_1, delimiter=",", lineterminator="\r", fieldnames=names)
    i = 0
    while i < 1000:
        x1 = random.random()
        x2 = random.random()
        x3 = random.random()
        m = multiply(x1, x2, x3)
        y = round(m, 5)
        file_writer.writerow({"x1": str(x1), "x2": str(x2), "x3": str(x3), "y": str(y)})
        i = i + 1

