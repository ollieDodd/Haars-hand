import cv2

path = 'haarcascades/open_Palm1.xml'
cam = 0
objname = 'HAND'
framew = 640
frameh = 480
color=(255,0,255)

cap = cv2.VideoCapture(cam)
cap.set(3,framew)
cap.set(4,frameh)

def empty(a):
    pass

cv2.namedWindow("Result")
cv2.resizeWindow("Result",framew,frameh+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,20,empty)
cv2.createTrackbar("Min Area", "Result",1,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)

cascade = cv2.CascadeClassifier(path)

while True:
    cameraB = cv2.getTrackbarPos("Brightness","Result")
    cap.set(10, cameraB)
    reg, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scaleVal = 1 +(cv2.getTrackbarPos("Scale","Result")/1000)
    neig = cv2.getTrackbarPos("Neig", "Result")
    objs = cascade.detectMultiScale(gray,scaleVal,neig)

    for(x,y,w,h) in objs:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area > minArea:
               cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
               cv2.putText(img,objname,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
               roi_color = img[y:y+h, x:x+w]
    cv2.imshow("result",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release
cv2.destroyAllWindows