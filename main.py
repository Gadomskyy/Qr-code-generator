import qrcode
import datetime

def qr_code_generation(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'{datetime.datetime}')

