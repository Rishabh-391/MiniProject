import cv2


# import numpy as np
def tracker():
    capture = cv2.VideoCapture("highway.mp4")
    # Object detection for a stable camera
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

    while True:
        ret, frame = capture.read()
        height, width, channel = frame.shape
        # print(height, width)
        # Create a Filter
        Filter = frame[200:350, 50:600]
        mask = object_detector.apply(Filter)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        # Extract coordinates of the white contours from mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        Detections_coordinates = []
        for i in contours:
            # Remove small elements on area basis
            area = cv2.contourArea(i)
            if area > 1000:
                # cv2.drawContours(Filter, [i], -1, (0, 255, 0))
                # Extracting the coordinates of the rectangles
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(Filter, (x, y), (x + w, y + h), (0, 255, 0), 2)
                Detections_coordinates.append([x, y, w, h])

        # Object Tracking
        # count = tracker.update(Detections_coordinates)
        for cnt in Detections_coordinates:
            x, y, w, h = cnt
            cv2.putText(Filter, "Motion", (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)
        cv2.imshow("FILTER", Filter)
        cv2.imshow("VIDEO", frame)
        cv2.imshow("MASK", mask)
        key = cv2.waitKey(30)
        if key == 27:  # esc key to close our window
            break

    capture.release()
    cv2.destroyAllWindows()
