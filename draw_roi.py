import numpy as np
import cv2
import pandas as pd

##define ROI function (we will use this to 1. detect light and 2. detect motion)

# Our ROI, defined by two points
p1, p2 = (), ()
state = 0


# Called every time a mouse event happen
def on_mouse(event, x, y, flags, userdata):
    global state, p1, p2

    # Left click
    if event == cv2.EVENT_LBUTTONUP:
        # Select first point
        if state == 0:
            p1 = (x, y)
            state += 1
        # Select second point
        elif state == 1:
            p2 = (x, y)
            state += 1
    # Right click (erase current ROI)
    if event == cv2.EVENT_RBUTTONUP:
        p1, p2 = (), ()
        state = 0


def __draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    color = (0, 0, 0)
    thickness = cv2.FILLED
    margin = 2
    txt_size = cv2.getTextSize(text, font_face, scale, thickness)
    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin
    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

def detection(vid, type, threshold, path):
    # Load video
    cap = cv2.VideoCapture(vid)
    cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
    count = 0
    light = []

    # Register the mouse click information
    cv2.setMouseCallback('Frame', on_mouse)

    if type == 'light':
        while cap.isOpened():
            ret, image = cap.read()

            if not ret:
                print('No frames grabbed!')
                break

            # If a ROI is selected, draw it
            if state > 1:
                image = cv2.rectangle(image, p1, p2, (255, 0, 0), 2)
            if (len(p2) > 0):
                roi = image[p1[1]:p2[1], p1[0]:p2[0]]
                mean_intensity = np.mean(roi)
                print("Mean intensity:", mean_intensity)
                # If mean intensity exceeds threshold, label it
                if (mean_intensity > threshold):
                    __draw_label(image, "light on {}th frame".format(count), (40, 20), (0, 255, 0))
                    light.append(count)
            cv2.imshow('Frame', image)
            count += 1
            # Show image
            k = cv2.waitKey(30) & 0xff
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        light_df = pd.DataFrame({'light_on' : light})
        light_df.to_csv(path)

    elif type == 'motion':
        mog = cv2.createBackgroundSubtractorMOG2()
        lick = []
        count = 0
        while cap.isOpened():
            ret, image = cap.read()

            if not ret:
                print('No frames grabbed!')
                break

            # If a ROI is selected, draw it
            if state > 1:
                image = cv2.rectangle(image, p1, p2, (255, 0, 0), 2)
            if (len(p2) > 0):
                roi = image[p1[1]:p2[1], p1[0]:p2[0]]
                fgmask = mog.apply(roi)
                # Analyze the motion mask to detect motion within the ROI
                motion_detection = cv2.countNonZero(fgmask)
                print(motion_detection)
                if (motion_detection > threshold):
                    __draw_label(image, "ROI: motion on {}th frame".format(count), (300, 20), (0, 0, 255))
                    lick.append(count)
            cv2.imshow('Frame', image)
            count += 1
            # Show image
            k = cv2.waitKey(30) & 0xff
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        lick_df = pd.DataFrame({'lick': lick})
        lick_df.to_csv(path)
