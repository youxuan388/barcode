import pyzbar.pyzbar as pyzbar

from PIL import Image

img = Image.open('test.jpg')

#img.show()

barcodes = pyzbar.decode(img)

for barcode in barcodes:
    print(barcode.data.decode('utf-8'))
    print(barcode.type)