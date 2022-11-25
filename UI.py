from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Git и желтые окружности(Нажмите ЛКМ!!!!)")
