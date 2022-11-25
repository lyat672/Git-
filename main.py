from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = -1
        self.y = -1
        self.k = 0
        self.setMouseTracking(True)
        self.colors = ['Yellow']

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.k = 1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.x > -1 and self.y > -1 and self.k == 1:
            qp.setBrush(QColor(choice(self.colors)))
            a = randint(1, 300)
            qp.drawEllipse(self.x, self.y, a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
