# SpotSpots

Running instructions
This project consists of four .py files: image_processing.py, training_model.py, CNN.py, predict.py

Run the files in following order:
1. image_processing.py processes the images using image processing techniques, and saves them in another folder for further processing.
2. training_model.py access the location in which image_processing.py saved the processed images and prepare them for training and save them using pickle
3. CNN.py uses convolutional neural networking to read the images and classify them into healthy and diseased leaves and save the model for further use.
4. predict.py predict images given by users if they are diseased or healthy using the model saved by CNN.py.

Test folder contains the images downloaded from google images search which will be classified.
