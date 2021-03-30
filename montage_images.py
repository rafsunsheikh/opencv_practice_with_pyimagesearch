from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help = "path to input directory of images")
ap.add_argument("-s", "--sample", type=int, default=21)
args = vars(ap.parse_args())

imagePaths = list(paths.list_images(args["images"]))
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

images = []

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)

montages = build_montages(images, (128,196), (7,3))

for montage in montages :
    cv2.imshow("Montage", montage)
    cv2.waitKey(0)

