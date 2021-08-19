from matplotlib import pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.axis('equal')
langs=['GiaoVienTH', 'GiangvienDH', 'Mang-Dientu', 'LapTrinh']
students=[12,2,3,4]
ax.pie(students, labels=langs,autopct='%1.2f%%')
plt.show()