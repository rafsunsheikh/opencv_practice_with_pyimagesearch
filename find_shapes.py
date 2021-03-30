import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# our goal : detect the black shapes in the image

lower = np.array([0,0,0])
upper = np.array([15,15,15])
shape_mask = cv2.inRange(image, lower, upper)

# cv2.imshow("shape_mask", shape_mask)
# cv2.waitKey(0)

cnts = cv2.findContours(shape_mask.copy(), cv2.RETR_EXTERNAL
                        , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    cv2.drawContours(image, [c], -1, (0,255,0), 2)
    cv2.imshow("image", image)
    cv2.waitKey(0)

# cv2.putText(image, "Found {} shapes".format(len(cnts)), (20, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
# cv2.waitKey(0)




