# Cheetah-Tracker
Non-Rigid  Object  Tracking  Based  on  CamShift  and  Particle-KalmanFilter

#### Use the link below to Download the Installers (for Ubuntu 16.04 (.deb)) 

https://drive.google.com/open?id=1SStLhS03HvJmlg0cUyrwXV297JC-JCvN

#### How to Use?

   1. Download and Install the 'CheetahTracker.deb' file.
   2. Open the Application and Load or Capture a Video.
   3. Click "Strat Tracker"; a widow named "Target Model Initialization" will pop-up. 
   4. Select the region of interest to track by dragging the mouse in the "Target Model Initialization" window.
   5. Tracking results will be shown in the GUI.
   6. The HSV histogram thresholds can also be controlled by moving the Slidebars of HSV Thresholding Window.

#### To run the Source Code the following requirements must be Satisfied

  1. Python (Version==3.5.2)
  2. OpenCV (Version==3.4.2.17) (with Contib modules)
  3. PyQt5 (Version==4.19.15)
  4. NumPy (Version==1.14.2)
  
##### # Note: Before running the source code, comment this line "from fbs_runtime.application_context.PyQt5 import ApplicationContext". This is a Library for creating Installers.
