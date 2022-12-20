import cv2
import numpy

while True :
    img=cv2.imread("image/berry.jpg")
    img=cv2.resize(img,(800,600))


    lower = numpy.array([29,37,181])
    upper = numpy.array([222,153,240])

    mask=cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)

cv2.destroyAllWindows()