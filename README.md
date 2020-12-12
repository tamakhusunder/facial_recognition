# facial_recognition_system

-This system is capable of recognizing the person as per the training the model 

-.ie. recognizing the online video as well as offline video and picture.

-This system is capable of capturing the person face as per required number,and save the picture in 220"*"220"*"3 size.

## Getting Start:
-Just run index_gui.py.

-index_gui is Gui that connect all other required part of feautres.

-Add faces folder if required in the project.


![Banner](https://github.com/tamakhusunder/Images/blob/master/magicball/face_recognization.jpg)

# Before update of this code:
Project of 7th sem

this is our mid defence code

VGG-16 architecture

used dlib for face recognization

run in spyder/jupyter

### 1.face-cap.ipynb:
-used to capture 1000 or as per required number and store in faces.

-add folder called 'faces' to run face-cap.ipynb.

### 2.model_training.ipynb:
-need folder of facesqq with validation folder and train folder inside it, to run model_training.ipynb.

-train the photo capture from face-cap or own dataset.
-save data in .md5

### 3.webcam_recognizer.ipynb:
-use to recognize the face train from model_training.

-load the data from .md5

### 4.index_gui.py:
-basic gui using tkinter

