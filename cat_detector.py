import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
ap.add_argument("-c", "--cascade", default="haarcascade_frontalcatface.xml", help="path to cat detector haar cascade")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1, minSize=(25,25))

for (i, (x, y, w, h)) in enumerate(rects):
    cv2.rectangle(image, (x,y), (x + w, y + h), (0,0,255), 2)
    cv2.putText(image, "Cat # {}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,0,255), 2)

cv2.imshow("cat Faces", image)
cv2.waitKey(0)

