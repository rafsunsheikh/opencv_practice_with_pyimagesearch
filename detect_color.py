import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boundaries = [
    ([17,15,100] , [50,56,200]),
    ([86,31,4] , [220,88,50]),
    ([25,146,90] , [62,174,250]),
    ([103,86,65] , [145,133,128])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype="uint8")
    # print(lower)
    upper = np.array(upper, dtype="uint8")
    # print(upper)

    mask = cv2.inRange(image, lower, upper)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
    output = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)