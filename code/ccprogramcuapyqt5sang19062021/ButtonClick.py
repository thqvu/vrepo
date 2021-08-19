import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QDialog()
    b1 = QPushButton(win)## Nút
    b1.setText("Nhập: Thêm, Xóa, Sửa")
    b1.setFont(QFont('Arial', 20))
    b1.move(50, 20)
    b1.clicked.connect(b1_clicked)

    b2 = QPushButton(win) ## Nút
    b2.setText("Hỏi đáp                   ")
    b2.setFont(QFont('Arial', 20))
    b2.move(50, 70)
    b2.clicked.connect(b2_clicked)

    b3 = QPushButton(win)  ## Nút
    b3.setText("Phân tích vẽ chart    ")
    b3.setFont(QFont('Arial', 20))
    b3.move(50, 120)
    b3.clicked.connect(b3_clicked)


    win.setGeometry(100, 100, 400, 200)

    win.setWindowTitle("Quản lý Bóng đá")
    win.show()
    sys.exit(app.exec_())


def b1_clicked():
    print("Button 1 clicked-Nhập thêm xóa sửa")


def b2_clicked():
    print("Button 2 clicked-Hỏi đáp ")

def b3_clicked():
    print("Button 3 clicked-phân tích vẽ biểu đồ")

if __name__ == '__main__':
    window()