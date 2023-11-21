# roi-detections
A simple OpenCV interface for light and motion detection within a drawn ROI.

![light_detection](https://github.com/vtsai881/roi-detections/assets/87097162/07c49325-ea52-4ee6-9603-5a14f851a173)![motion_detection](https://github.com/vtsai881/roi-detections/assets/87097162/e0a03b3a-1e66-491d-bafd-745f49328f32)



# Key Features
- draw a rectangle ROI of any size directly onto your video of interest
- set a threshold for motion or light detection 
- save frames in which light or motion is detected

# Getting Started
1. download and run _draw_roi.py_
2. to run roi detection, run `detection(vid, type, threshold)`
   - tip: to use your video webcam, set `vid` as `0`
4. a separate window for the videofeed should open.
5. draw your roi by clicking the point that you want to be the top left corner of the roi followed by the point you want to be the bottom right corner of the roi. this should draw a blue rectangle roi on the frame.
6. to delete a drawn roi, right click and the blue box should disappear.
7. once an roi is drawn, between frame motion or pixel intensity will be calculated within it. frames in which motion or intensity is greater than the given threshold will be labeled **ROI: motion/light on {}th frame** and saved to your output csv.
8. close the window by hitting `q` on the keyboard. this may take multiple tries if you haven't selected the video feed window.
9. detection will keep running until the last frame in the video or until the window is closed.
10. detected frames will be saved in a csv to the file path specified!
 
# Dependencies
OpenCV, numpy, pandas
