# Importing opencv
import cv2
import datetime
import math


# instance of video capture
def record():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Checking if the camera is opened or not
    opened = cap.isOpened()
    # fourcc - four character code for determining the codec of the video file
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # Getting the properties of the video using video capture instance
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    t = datetime.datetime.now().time()
    hrs = math.fmod(t.hour, 12)
    minute = t.minute
    second = t.second
    # output video writer creation
    out = cv2.VideoWriter('recordedvid' + str(hrs) + str(minute) + str(second) + '.avi',
                          fourcc, fps, (int(width), int(height)))
    print("Frames are {}".format(fps))
    # Showing and storing the live camera feed
    # Check if camera is opened
    if opened:
        # Run until it remains open
        while cap.isOpened():
            # Get the frame from Video capture Instance
            ret, frame = cap.read()
            # return ret Variable tells if the frame is returned successfully
            if ret:
                cv2.imshow('winname', frame)
                # Writing the frame to video output
                out.write(frame)
                # Wait for 2 milliseconds for each frame
                # If user press 'esc' key then exit loop
                if cv2.waitKey(2) == 27:
                    break

    out.release()
    cap.release()

    cv2.destroyAllWindows()
