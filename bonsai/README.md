# Bonsai Implementation
A [Bonsai](https://bonsai-rx.org/) interface for the roi-detection function using the Bonsai [Python Scripting](https://bonsai-rx.org/python-scripting/) package. 

# Key Features
- allows you to detect motion or light intensity real time
- aligns csv results with arduino, ttl or other bonsai-centralized outputs

# Getting Started
1. download Bonsai and install the **Bonsai - Python Scripting Package**
2. create a Python environment to run Bonsai in with the required dependencies:
   ```
   conda create --name bonsai-env python=3.8 numpy pandas opencv-python
   ```
   - tip: **python must be 3.8!** python 3.9 and python 3.10 currently do not seem to be compatible with Bonsai's pythonnet backend
4. activate your environment, navigate to the folder with your Bonsai installation, then launch Bonsai:
   ```
   conda activate bonsai-env
   cd C:\Users\Valerie\AppData\Local\Bonsai
   bonsai
   ```
5. open _roi-detection.bonsai_ this should be installed in a folder together with _roi-detection.bonsai.layout_
6. the Bonsai layout should look like this: 
  ![image](https://github.com/vtsai881/roi-detections/assets/87097162/4546e48b-d0b3-4fcb-a254-de62c2e92f27)

7. the top section creates a connection to an arduino, reading a csv with a specified arduino protocol, and writing outputs from the arudino to a csv:
   ![image](https://github.com/vtsai881/roi-detections/assets/87097162/34557fa3-52a2-4e5c-bd9e-c2086f70a182)
8. the bottom section creates a Python runtime, loads relevant scripts, then runs code specified in  **_Exec_**:
  ![image](https://github.com/vtsai881/roi-detections/assets/87097162/10c5143c-8d0b-4056-9fe0-2d1e7858cbb9)
9. set **PythonHome** in **_CreateRuntime_** to the path to your environment (typically in _anaconda3\envs\yourenv_ or _.conda\envs\yourenv_ ) and set **ScriptPath** to the path to _draw_roi.py_ (downloadable from the main folder) 
   ![image](https://github.com/vtsai881/roi-detections/assets/87097162/0345e697-31a4-479c-8a48-cef5e8edc8ad)
10. to run roi detection, write `detection(vid, type, threshold, savepath)` (with your specified parameters) in the **Script** box of **_Exec_**:
    ![image](https://github.com/vtsai881/roi-detections/assets/87097162/5e61465e-6f5a-4f5d-9087-9128b4e2a93b)
    - tip: you must hit `CTRL-ENTER` for this code to save.
    - tip2: the _vid_ parameter of `detection()` should be set to 0 to record from the webcam.
11. run Bonsai workflow.
