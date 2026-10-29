import qrcode

from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4)
qr.add_data("https://www.minecraft.net/en-us")
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="green"
)

img.save("qr_diff.png")