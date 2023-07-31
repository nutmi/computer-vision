import cv2


coin_detect = cv2.CascadeClassifier('cascade.xml')
coin_img = cv2.imread('25498.jpg', cv2.IMREAD_UNCHANGED)

gray_img = cv2.cvtColor(coin_img, cv2.COLOR_BGR2GRAY)
faces = coin_detect.detectMultiScale(gray_img, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(coin_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
coin_img = cv2.resize(coin_img, (1920, 1080))
cv2.imshow("img",coin_img)
cv2.waitKey()
cv2.destroyAllWindows()