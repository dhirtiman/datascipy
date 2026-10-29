import qrcode
data = "https://google.com"
qr = qrcode.make(data)
qr.save("qr_code.png") # type: ignore
print("qr code saved")