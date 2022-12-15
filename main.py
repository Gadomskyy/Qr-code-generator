import qrcode
from _datetime import datetime

def qr_code_generation(text):
    curr_date = datetime.now()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'QR_Code_{curr_date.year}-{curr_date.month}-{curr_date.day}_{curr_date.hour}-{curr_date.minute}-{curr_date.second}.png')

# def main():
#     qr_code_generation('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#
# if __name__ == "__main__":
#     main()