import cv2
import numpy as np
import face_recognition
import os
import pickle
from datetime import datetime

path = '../ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)

for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    with open('dataset_faces.dat','wb') as f:
        pickle.dump(encodeList,f)
    # return encodeList

findEncodings(images)
print('Encoding complete')