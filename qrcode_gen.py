import qrcode
from _datetime import datetime


class Qrcode_gen():
    
    def __init__(self, text):
        self.text = text
        self.img = None

    def qr_code_generation(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(self.text)
        self.img = qr.make_image(fill_color="black", back_color="white")

    def save_img(self):
        curr_date = datetime.now()
        self.img.save(f'QR_Code_{curr_date.year}-{curr_date.month}-{curr_date.day}_{curr_date.hour}-{curr_date.minute}-{curr_date.second}.png')

qr = Qrcode_gen('https://www.youtube.com/')
qr.qr_code_generation()
qr.save_img()