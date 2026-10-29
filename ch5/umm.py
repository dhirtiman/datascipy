import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# 1. Initialize QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=3)
qr.add_data('https://forms.gle/GFSJsWy7PFBUftxBA')
light = 50
# 2. Make the styled image
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(back_color=(28, 180, 60), center_color=(0, 0, 0), edge_color=(1, 1, 1)),
    embeded_image_path="./c.png" 
)

# 3. Save the image
img.save('cc.png')
