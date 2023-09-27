import requests
from io import BytesIO
import os
import qrcode
from PIL import Image, ImageDraw, ImageDraw2, ImageFont
import urllib.request

# get my ip addr
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# Get the fonts 
# req = requests.get("https://github.com/googlefonts/zen-antique/blob/main/fonts/ttf/ZenAntique-Regular.ttf?raw=true")
# font = ImageFont.truetype(BytesIO(req.content), 72,)
font = ImageFont.truetype("Caveat/Caveat-VariableFont_wght.ttf", 64)

ip = f'http://{external_ip}:5000'

files = os.listdir('templates')
    
for line in files:
    line = os.path.splitext(line)[0]
    if len(line) > 3:
        continue
    print(ip + '/' + line)
    img = qrcode.make(ip + '/' + line)
    im1 = Image.new('RGB',
                 (335, 400),   # A4 at 72dpi
                 (255, 255, 255))  # White
    im1.paste(img, img.getbbox())
    draw = ImageDraw.Draw(im1)
    draw.text((50, 295), "Adventure", font=font, align="center", fill='black')
    im1.save("qr_codes/" + line + ".png")