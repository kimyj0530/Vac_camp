import cv2
# 동영상 처리
# 영상 읽기, 영상 출력
cap = cv2.VideoCapture(0) # 첫번째 웹캠을 불러옴
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read() # ret = return, frame = 이미지객체
    if ret :
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): # q입력시 break
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

mpf = cv2.VideoCapture('data/crowd.mp4')
print(mpf.isOpened())
while(mpf.isOpened()):
    ret, frame = mpf.read()
    if ret :
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

mpf.release()
cv2.destroyAllWindows()