import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()
      self.initUI()

   def initUI(self):
      self.text = "Chào buổi sáng!"
      self.setGeometry(100,100, 500,300)
      self.setWindowTitle('Draw Demo ĐH Lạc Hồng')
      self.show()

   def paintEvent(self, event):
      qp = QPainter()
      qp.begin(self)
      qp.setPen(QColor(Qt.red))
      qp.setFont(QFont('Arial', 20))
      qp.drawText(10,50, "Chào buổi sáng!")
      qp.setPen(QColor(Qt.blue))
      qp.drawLine(10,100,100,100) ## Ve khung
      qp.drawRect(10,150,150,100) ## Ve hinh chu nhat
      qp.setPen(QColor(Qt.yellow))
      qp.drawEllipse(100,50,100,50)
      ## Ve picture lay tu ngoai
      qp.drawPixmap(220,10,QPixmap("New_Ronaldo.png"))
      qp.fillRect(20,175,130,70,QBrush(Qt.SolidPattern))
      qp.end()

def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()