import cv2
import os
import numpy as np

# image processing of with black spot disease
for image in os.listdir(
        './Citrus/Leaves/Black spot'):
    img = cv2.imread(os.path.join(
        './Citrus/Leaves/Black spot', image))

    img = cv2.resize(img, (256, 256))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, threshh = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY_INV +
                                 cv2.THRESH_OTSU)

    '''cv2.imshow(image, threshh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(threshh, cv2.MORPH_CLOSE,
                               kernel, iterations=2)

    dst = cv2.bitwise_and(gray, closing)

    path = './Data/Black spot'
    cv2.imwrite(os.path.join(path, image), dst)

    '''cv2.imshow(image, dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

# Healthy leaves
for himage in os.listdir(
        './Citrus/Leaves/healthy'):
    himg = cv2.imread(os.path.join(
        './Citrus/Leaves/healthy', himage))

    himg = cv2.resize(himg, (256, 256))
    hgray = cv2.cvtColor(himg, cv2.COLOR_BGR2GRAY)

    ret, threshh = cv2.threshold(hgray, 0, 255,
                                 cv2.THRESH_BINARY_INV +
                                 cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(threshh, cv2.MORPH_CLOSE,
                               kernel, iterations=2)

    dsth = cv2.bitwise_and(hgray, closing)

    path = './Data/Healthy'
    cv2.imwrite(os.path.join(path, himage), dsth)
