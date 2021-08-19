#https://pythonspot.com/en/matplotlib-legend/
### Program Name: VebieudoCacDoiBongWorldCup.py
### Date: June 12,2021
### Chuong trinh ve chart de phuc vu chuc nang phan tich du lieu bong da
#### BARotlib.pyplot as plt; plt.rcdefaults()

# BAR chart

import numpy as np
import matplotlib.pyplot as plt

objects = ('Vietnam', 'Thailand', 'UAE', 'Malaysia', 'Indonesia')
y_pos = np.arange(len(objects)) ## Gia tri là 5
performance = [17,9,15,9,1] ## Chieu cao cua tung cot trong bieu do

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects) ## Tieu de tren truc X
plt.ylabel('Số trận thắng') ## Nhan tren truc Y
plt.title('Phân tích số điểm của các đội thuộc bảng G')

plt.show()
