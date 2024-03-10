import pandas as pd
from keras import Sequential, Model, Input
from keras.src.layers import Dense
import tensorflow

# Чтение данных из CSV-файла
data = pd.read_csv('data_mul_2.csv', header=None)

# Разделение данных на признаки (X) и целевую переменную (y)
x = data.iloc[:, :-1].values  # Признаки - все столбцы кроме последнего
y = data.iloc[:, -1].values   # Целевая переменная - последний столбец

# Определение входных данных для каждого нейрона на первом слое
input_x1 = Input(shape=(1,))
input_x2 = Input(shape=(1,))
input_x3 = Input(shape=(1,))

# Создание слоев для каждого из нейронов, принимающих соответствующий вход
neuron_x1 = Dense(units=1, activation='sigmoid')(input_x1)
neuron_x2 = Dense(units=1, activation='sigmoid')(input_x2)
neuron_x3 = Dense(units=1, activation='sigmoid')(input_x3)

# Объединение выходов нейронов во втором слое
merged_layer = Dense(units=1, activation='linear')(neuron_x1 + neuron_x2 + neuron_x3)

# Создание третьего слоя с функцией активации сигмоид
output_layer = Dense(units=1, activation='sigmoid')(merged_layer)

# Создание модели
model = Model(inputs=[input_x1, input_x2, input_x3], outputs=output_layer)

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='SGD', metrics=['accuracy'])

# Вывод информации о структуре модели
model.summary()

# Обучение модели
result = model.fit([x[:,0], x[:,1], x[:,2]], y, epochs=10, batch_size=1, verbose=1)

print("Коэффициент a после обучения нейросети:", model.layers[-1].get_weights()[0][0][0])
