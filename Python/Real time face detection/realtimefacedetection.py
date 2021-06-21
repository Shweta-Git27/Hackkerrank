import cv2
alg = "haarcascade_frontalface_default.xml"
haar = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w , y+h),(0,255,0),2)
    cv2.imshow("facedetection",img)
    key = cv2.waitKey(20)
    if key == 30:
        break
cam.release()
cv2.destroyAllWindows()
        
