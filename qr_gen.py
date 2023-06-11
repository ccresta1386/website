import requests
from io import BytesIO
import qrcode
from PIL import Image, ImageDraw, ImageDraw2, ImageFont

# Get the fonts 
# req = requests.get("https://github.com/googlefonts/zen-antique/blob/main/fonts/ttf/ZenAntique-Regular.ttf?raw=true")
# font = ImageFont.truetype(BytesIO(req.content), 72,)
font = ImageFont.truetype("Caveat\Caveat-VariableFont_wght.ttf", 64)

ip = 'http://173.71.158.88:5000'
f = open('site_list.txt')


lines = f.readlines()
for line in lines:
    line = line.strip()
    img = qrcode.make(ip + '/' + line)
    im1 = Image.new('RGB',
                 (335, 400),   # A4 at 72dpi
                 (255, 255, 255))  # White
    im1.paste(img, img.getbbox())
    draw = ImageDraw.Draw(im1)
    draw.text((50, 295), "Adventure", font=font, align="center", fill='black')
    im1.save("qr_codes/" + line + ".png")