import cv2

import pyzbar.pyzbar as pyzbar

cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)

camera = cv2.VideoCapture(0)

while(True):
    ret,frame = camera.read()
    cv2.imshow("camera",frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        print(f"{barcode.type}:{barcode.data.decode('utf-8')}")
    
    
    if(cv2.waitKey(5)==27):#當esc被我按下
        break

camera.release()

cv2.destroyAllWindows()
