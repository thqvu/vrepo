### Program Name:MenuDrivenProgram.py
### Author: Hung bóng đá
### Date: June 12,2021
### Ghi chu: Chuong trinh nay co nhieu chuc nang de quan ly bong da

### Chia se mot file chung abc.txt
### Chuc nang 1: Nhap
def Nhap():
    print("=== Chuc nang nhap, ghi file abc.txt ===")
    return

### Chuc nang 2: Hoi Dap
def Hoidap():
    print("==== Chuc nang hoi dap, doc file abc.txt de tra loi===")
    return

### Chuc nang 3: Phan tich
def PhantichBieuDo():
    print("===Chuc nang phan tich, doc file abc.txt de tra loi====")
    from matplotlib import pyplot as plt
    import numpy as np
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    langs = ['GiaoVienTH', 'GiangvienDH', 'Mang-Dientu', 'LapTrinh']
    students = [12, 2, 3, 4]
    ax.pie(students, labels=langs, autopct='%1.2f%%')
    plt.show()
    return

def Menu(chon):
    switcher = {
        1: Nhap,
        2: Hoidap,
        3: PhantichBieuDo,
    }
    # Get the function from switcher dictionary
    func = switcher.get(chon, lambda: "Du lieu sai")
    # Execute the function
    func()

while True:
    print("")
    chon=int(input("Cho chuc nang 4 de ket thuc="))
    if chon > 3 :
        break
    Menu(chon)

print("Chao tam biet")