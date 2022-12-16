from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('qr_code_gui.ui', self)
        self.show()

        #Connecting the Save, Load, Exit options from File menu to methods
        self.actionSave.triggered.connect(self.save_qr)
        self.actionLoad.triggered.connect(self.load_qr)
        self.actionExit.triggered.connect(self.exit_program)

        #Connecting the push buttons to menus
        self.convert_into_QR.clicked.connect(self.make_qr)
        self.convert_into_text.clicked.connect(self.make_text)

    def save_qr(self):
        pass

    def load_qr(self):
        pass

    def exit_program(self):
        sys.exit()

    def make_qr(self):
        pass

    def make_text(self):
        pass

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()