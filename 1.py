import cv2 # cv2 패키지를 불러옴
# 이미지 불러오기
img = cv2.imread('data/Dog.jpg')
cv2.imshow('dog', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

