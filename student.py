import cv2

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detectmultiscale returns the rectangle with coordiantes(x,y,w,h)
faces = face_cascade.detectMultiScale(gray,1.1,3)
print(len(faces))

for (x,y,w,h) in faces:
        # cv2.rectangle(image,startpoint,endpoint,color(BGR),thickness of the reactangel border)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,160,240),4)
#        # crop the image to save the face image
#        # in array format the image takesin height first and then width
#        roi_color=img[y:y+h,x:x+w]
#        cv2.imwrite("face.jpg",roi_color)             
cv2.imshow('img',img)
cv2.waitKey(0)