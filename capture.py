import cv2, time

# the number_of_frames_captured variable is just part of the dev code
# it will show you how many frame shots are captured. Remove before delivery

number_of_frames_captured = 0

while True:
    number_of_frames_captured = number_of_frames_captured+1

    video = cv2.VideoCapture(0)
    check, frame = video.read()
    #check is checking that a video camera is present. This will be expanded
    #later, to handle errors (e.g. If false, then message to user)

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(gray, "Number of frames: %s" % number_of_frames_captured,
               (250, 450),
    cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Capturing", gray)
    #converting the captured image to greyscale as easier to handle

    key = cv2.waitKey(100)
    #how long it the camera will keep capturing. Change the milsecs for longer
    #press q on the keyboard to stop capture, as currently in a while loop
    if key == ord('q') or number_of_frames_captured == 33:
        break

print(number_of_frames_captured)
video.release()
cv2.destroyAllWindows()
