from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        ## Menu Ngang
        actionFile = menubar.addMenu("Nhập")
        ## Menu doc cua menu File
        actionFile.addAction("Thêm")
        actionFile.addAction("Xóa")
        actionFile.addAction("Sửa")
        actionFile.addSeparator()
        actionFile.addAction("Kết thúc")
        ## Menu Ngang
        actionEdit=menubar.addMenu("Hỏi đáp")
        actionEdit.addAction("Theo tên")
        actionEdit.addAction("Theo tuổi")
        ## Menu Ngang
        actionView=menubar.addMenu("Biểu đồ")
        actionView.addAction("Vẽ biểu đồ")

        ## Menu Ngang
        actionHelp=menubar.addMenu("Trợ giúp")
        actionHelp.addAction("Trợ giúp chi tiết")
        # add textbox
        tbox = QPlainTextEdit()
        layout.addWidget(tbox, 1, 0)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())