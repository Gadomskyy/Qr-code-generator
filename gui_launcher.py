from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('qr_code_gui.ui', self)
        self.show()

        self.actionSave.triggered.connect(self.save_qr)
        self.actionLoad.triggered.connect(self.load_qr)
        self.actionExit.triggered.connect(self.exit_program)

    def save_qr(self):
        pass

    def load_qr(self):
        pass

    def exit_program(self):
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()