import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
   app = QApplication(sys.argv)
   w = QWidget() ## Cửa sổ
   b = QLabel(w) ## Nhãn
   b.setText("Chào Việt Nam!")
   w.setGeometry(100,100,200,50) ## Thiet lap cua so
   b.move(50,20)
   w.setWindowTitle("Hệ chương trình quản lý bóng đá, 2021")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window() ## Loi goi ham