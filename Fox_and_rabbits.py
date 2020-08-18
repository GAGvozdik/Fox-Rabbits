from matplotlib.pyplot import *

fig = figure()
# положение графиков
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# параметры модели
a = 50
b = 25
c = 20
e = 8

# начальные популяции лис и кроликов
Ro = 15
Fo = 5

# число измерений
quantity_of_measurements = 50000

# длина наблюдения
lenght_obs = 1.5

# элементарный отрезок времени между измерениями
h = lenght_obs / quantity_of_measurements

# массив времени
t = []

# массивы с популяциями лис и кроликов
Rabbits_mass = [Ro]
Fox_mass = [Fo]

for i in range(quantity_of_measurements):
    # добавляю текущее время в массив времени
    t.append(i * h)

    # добавляю "пустой" элемент
    Rabbits_mass.append(1)
    Fox_mass.append(1)

    # у-ря популяции
    Rabbits_mass[i + 1] = Rabbits_mass[i] + h * (a - b * Fox_mass[i]) * Rabbits_mass[i]
    Fox_mass[i + 1] = Fox_mass[i] + h * (-c + e * Rabbits_mass[i]) * Fox_mass[i]

# графики популяций от времени
ax1.scatter(t, Rabbits_mass[0:-1], s=1, color='blue')
ax1.scatter(t, Fox_mass[0:-1], s=1, color='green')

# фигура лиссажу
ax2.scatter(Rabbits_mass, Fox_mass, s=1, color='green')

show()
