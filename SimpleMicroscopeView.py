import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open microscope camera")

while True:
    ret, frame = cap.read()
    cv2.imshow('Input',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame.release()
cv2.destroyAllWindows()
