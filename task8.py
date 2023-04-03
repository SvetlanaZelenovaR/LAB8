# Вариант 9

import cv2


# Задание 1
img = cv2.imread('variant-9.png')
pyramid1 = cv2.pyrDown(img)
pyramid2 = cv2.pyrDown(pyramid1)

cv2.imshow('img1', img)
cv2.imshow('img2', pyramid1)
cv2.imshow('img3', pyramid2)

fly = cv2.imread('fly64.png')
fly = cv2.cvtColor(fly, cv2.COLOR_BGR2GRAY)

# Задание 2
cap = cv2.VideoCapture(0)
down_points = (640, 480)
coor = []
sm_x = 0
sm_y = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        coor.append([x, y])
        rec = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
        rec[y:y + fly.shape[0], x:x + fly.shape[1]] = fly  # Доп. задание

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        for i in range(len(coor)):  # Задание 3
            sm_x += coor[i][0]
            sm_y += coor[i][1]
        print(sm_x // len(coor), sm_y // len(coor))
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
