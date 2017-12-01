import cv2
import numpy

capture = cv2.VideoCapture(0)

while True:
    ret, image = capture.read()
    (_, w, _) = image.shape
    scale = 640.0 / w
    image = cv2.resize(image, (0,0), fx=scale, fy=scale)
    (h, w, _) = image.shape

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blured = cv2.medianBlur(grey, 15)
    
    t = 100
    sc = 1
    md = 30
    at = 40
    circles = cv2.HoughCircles(blured, cv2.HOUGH_GRADIENT, sc, md, t, at)
    
    if circles is not None:
        # We care only about the first circle found.
        circle = circles[0][0]
        x, y, radius = int(circle[0]), int(circle[1]), int(circle[2])
        # Highlight the circle
        cv2.circle(image, (x, y), radius, (0, 0, 255), 1)
        # Draw a dot in the center
        cv2.circle(image, (x, y), 1, (0, 0, 255), 1)

    cv2.imshow('Camera stream', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

server.close()