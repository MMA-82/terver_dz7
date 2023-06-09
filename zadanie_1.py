# Задача 1. Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции, имеются ли статистические различия между группами?

import numpy as np
import scipy.stats as stats

x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

print(stats.mannwhitneyu(x1, y1))

# Вывод: p-value > alpha - статистически значимые различия не выявлены на уровне значимости alpha = 0,05
