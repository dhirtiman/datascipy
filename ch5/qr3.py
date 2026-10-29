import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image
qr = qrcode.QRCode(
    version=10,# 1-40
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4)
qr.add_data("https://forms.gle/GFSJsWy7PFBUftxBA")
qr.make(fit=True)
img = qr.make_image(fill_color="#593dd3", back_color="white").convert("RGB")
logo = Image.open("c.png").convert("RGBA")
# resize logo to fit in the QR code
qr_width, qr_height = img.size
logo_size = int(qr_width *0.20)
logo = logo.resize((logo_size,logo_size),Image.Resampling.LANCZOS)
# paste logo on the QR code
padding = 10
# position
position = (
    (qr_width - logo_size)//2,
    (qr_height - logo_size)//2
)
img.paste(logo, position, logo)
img.save("gform.png")

