## Creates a qrcode using an inputted link 'text' and saves it as "qrcode.png"

import qrcode

def qrcode_generate(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
        )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrcode.png")
    
url = input("Enter your url: ")
qrcode_generate(url)