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
        self.convert_into_text.clicked.connect(self.read_qr)


    def load_qr(self):
        #opens file selection window
        response, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption='Select a file',
                                                         directory=os.getcwd(),
                                                         filter='Image file (*.png)'
                                                         )
        #Creates image of loaded file
        pixmap = QtGui.QPixmap(response)
        pixmap = pixmap.scaled(200, 200)
        self.qr_code_display.setScaledContents(True)
        self.qr_code_display.setPixmap(pixmap)
        #Clears the input line after loading file to avoid confusion
        self.textLine.clear()

    def save_qr(self):
        #opens file save window
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(parent=self,
                                                         caption='Save a file',
                                                         directory=os.getcwd(),
                                                         )
        #Saves the image from the display as png
        if filename != '':
            img = self.qr_code_display.pixmap()
            img.save(f'{filename}.png')


    def exit_program(self):
        #Creates a message box confirming if the user wants to quit when using Exit button
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Exit the program?')
        msg.setText('Are you sure you want to quit?')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.Yes)

        x = msg.exec_()
        if x == QtWidgets.QMessageBox.Yes:
            sys.exit(0)
        else:
            pass


    def make_qr(self):
        #creates QR object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=2,
        )

        #adds data from input file into qr object
        qr.add_data(self.textLine.toPlainText())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('sample.png')
        #loads created qr code
        pixmap = QtGui.QPixmap('sample.png')
        pixmap = pixmap.scaled(200, 200)
        self.qr_code_display.setScaledContents(True)
        self.qr_code_display.setPixmap(pixmap)
        #removes created qr code after loading it to avoid unwanted files
        os.remove('sample.png')

    def read_qr(self):
        current_img = self.qr_code_display.pixmap()
        current_img.save('temporaryforload.png')
        self.currentfile = os.path.abspath('temporaryforload.png')
        img = cv2.imread(self.currentfile)
        detect = cv2.QRCodeDetector()
        data, _, _ = detect.detectAndDecode(img)
        #if we cant decode QR code, throw a popup message
        if not data:
            err_msg = QtWidgets.QMessageBox()
            err_msg.setWindowTitle('QR code not recognized')
            err_msg.setText("Not able to detect the QR code. Please make sure the loaded image is correct and try again.")
            err_msg.setIcon(QtWidgets.QMessageBox.Warning)
            err_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            x = err_msg.exec_()

        self.textLine.setText(data)
        #is there a way to do it without dummy files?
        os.remove('temporaryforload.png')
        #TODO: implement a warning when file is not recognizable


#TODO: make an .exe file of the program
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()