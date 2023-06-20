"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies? 
"""


import pandas as pd 
import numpy as np
import random

""" # Перевод данных в one hot вид без pandas 
def one_hot_view (lst):
    count = 1
    print('N','\t', 'Data', '\t', 'human','\t','robot')
    for i in lst:
        print(f'{count}', '\t', f'{i}','\t','1' if i == 'human' else '0', '\t', '1' if i == 'robot' else '0') 
        count += 1 """

# Перевод данных используя pandas 

""" lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst}) """
""" one_hot_view(lst) """



d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(d)


print(df)