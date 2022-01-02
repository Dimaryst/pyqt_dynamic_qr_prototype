import sys
import pyqrcode
import qdarkstyle
from PyQt5 import QtWidgets, QtGui
from prot_design import Ui_MainWindow


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEditLine.textChanged.connect(self.update_qr)

    def update_qr(self):
        qr = pyqrcode.create(self.textEditLine.text())
        qr.png('qr.png', scale=8)
        self.label.setPixmap(QtGui.QPixmap("qr.png"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
