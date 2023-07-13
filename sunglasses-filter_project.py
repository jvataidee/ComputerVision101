import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

glassPNG = cv2.imread('sunglass.png', -1)

def add_sunglasses(frame, gray):
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eyesCascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            eyes = sorted(eyes, key=lambda x: x[0])
            glasses_width = int(2.5 * abs(eyes[0][0] - eyes[1][0]))
            glasses_height = int(0.8 * h)

            glasses_color = glassPNG[:, :, :3]
            glasses_alpha = glassPNG[:, :, 3]

            glasses_color_resized = cv2.resize(glasses_color, (glasses_width, glasses_height), interpolation=cv2.INTER_CUBIC)
            glasses_alpha_resized = cv2.resize(glasses_alpha, (glasses_width, glasses_height), interpolation=cv2.INTER_CUBIC)

            roi = frame[y:y+glasses_height, x:x+glasses_width]

            masked_region = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(glasses_alpha_resized))
            masked_glasses = cv2.bitwise_and(glasses_color_resized, glasses_color_resized, mask=glasses_alpha_resized)

            frame[y:y+glasses_height, x:x+glasses_width] = cv2.add(masked_region, masked_glasses)

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_with_sunglasses = add_sunglasses(frame, gray)
        cv2.imshow('Sunglasses Filter', frame_with_sunglasses)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
