import cv2
image=cv2.imread('pic.jpg',1)
cv2.line(image,(0,0),(200,200),(255,0,0),4)
cv2.line(image,(0,200),(200,0),(255,0,0),4)
cv2.rectangle(image,(0,0),(200,200),(0,255,0),3)
cv2.circle(image,(100,100),100,(0,0,255),-1)
font=cv2.FONT_ITALIC
cv2.putText(image,"hello",(0,200),font,4,(255,255,255),cv2.LINE_AA)
cv2.imshow("shapes",image)
cv2.waitKey(0)
cv2.destroyAllWindows()