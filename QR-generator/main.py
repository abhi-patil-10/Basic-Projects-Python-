import qrcode
from PIL import Image, ImageDraw

url = input("Enter the url : ")
file_name = input("Enter the filename :")

if not(file_name.endswith(".png")):
    file_name = file_name + ".png"

img = qrcode.make(url)
img.save(file_name)