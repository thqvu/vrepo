import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    w = QWidget()  ## Cua so
    b = QPushButton(w) ## Nút
    b.setText("Hiển thị message!")

    b.move(100, 50) ## X=100 y =50
    b.clicked.connect(showdialog) ### Xu ly Click vao nút
    w.setWindowTitle("PyQt Đại học Lạc Hồng - MessageBox demo")
    w.show()
    sys.exit(app.exec_())

## Ham nay duoc thuc hien khi chung ta click vao node
def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()


def msgbtn(i):
    print("Button pressed is:", i.text())


if __name__ == '__main__':
    window()