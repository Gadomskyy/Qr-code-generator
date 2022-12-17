from PyQt5 import QtWidgets, uic, QtGui
import sys
import os
import qrcode
import cv2


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('qr_code_gui.ui', self)
        self.show()
        self.setFixedSize(712, 360)

        #Connecting the Save, Load, Exit options from File menu to methods
        self.actionSave.triggered.connect(self.save_qr)
        self.actionLoad.triggered.connect(self.load_qr)
        self.actionExit.triggered.connect(self.exit_program)

        #Connecting the push buttons to menus
        self.convert_into_QR.clicked.connect(self.make_qr)
        self.convert_into_text.clicked.connect(self.make_text)


    def load_qr(self):
        response, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption='Select a file',
                                                         directory=os.getcwd(),
                                                         filter='Image file (*.png)'
                                                         )
        pixmap = QtGui.QPixmap(response)
        pixmap = pixmap.scaled(200, 200)
        self.qr_code_display.setScaledContents(True)
        self.qr_code_display.setPixmap(pixmap)

    def save_qr(self):
        pass

    def exit_program(self):
        sys.exit(0)

    def make_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=2,
        )

        qr.add_data(self.textLine.toPlainText())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('sample.png')
        pixmap = QtGui.QPixmap('sample.png')
        pixmap = pixmap.scaled(200, 200)
        self.qr_code_display.setScaledContents(True)
        self.qr_code_display.setPixmap(pixmap)
        os.remove('sample.png')

    def make_text(self):
        pass

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()