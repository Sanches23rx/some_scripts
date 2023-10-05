import pandas as pd
import numpy as np

# Открытие исходного текстового файла
with open('./test.txt', 'r', encoding='utf8') as f:
    str1 = f.read()
all_freq = {}

# Создание словаря "символ" - "количество"
for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# Создание отдельных массивов для символов, количества вхождений и процентов от общего количества
symbols = []
counts = []
percentages = []
for i in range(len(all_freq)):
    symbols.append(list(all_freq)[i])
    counts.append(all_freq[list(all_freq.keys())[i]])
    percentages.append(round((counts[i]/len(str1))*100, ndigits=1))

# Создание и сортировка итогового датафрейма
data = [symbols, counts, percentages]
df = pd.DataFrame(data, index=['symbols', 'count', 'percentage'], columns=np.arange(1,38))
df = df.T
df_sort = df.sort_values(by=['count'], ascending=False, ignore_index=True)
print(df_sort)

