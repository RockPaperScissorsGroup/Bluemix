import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
width = 1080
cv2.namedWindow("frame", 0)
cv2.resizeWindow("frame", width, 768)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        ts = time.time()
        r = 1080.0 / frame.shape[1]
        dim = (1080, int(frame.shape[0] * r))

        # perform the actual resizing of the image and show it
        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite('images/newImage_' + str(ts) + '.png', resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
