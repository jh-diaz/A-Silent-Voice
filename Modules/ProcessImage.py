import cv2
import numpy
from Modules.OpenCVWrapper import createNewWindow, createTrackbar, displayImage

BOX_Y = 80
BOX_X = 80
BOX_WIDTH = 300  # 300
BOX_HEIGHT = 300  # 300

SHOW_ACC = False

def showAcc(bool):
    global SHOW_ACC
    SHOW_ACC = bool

def changeROIPlacement(x,y):
    BOX_X = x
    BOX_Y = y

# Turns an RGB image into a thresholded black and white images
# where white colors are darkened and everything else is white
def thresholdHSVBackground(image):
    l_h = cv2.getTrackbarPos('L - h', 'HSV Values')
    u_h = cv2.getTrackbarPos('U - h', 'HSV Values')
    l_s = cv2.getTrackbarPos('L - s', 'HSV Values')
    u_s = cv2.getTrackbarPos('U - s', 'HSV Values')
    l_v = cv2.getTrackbarPos('L - v', 'HSV Values')
    u_v = cv2.getTrackbarPos('U - v', 'HSV Values')

    MIN_HSV = numpy.array([l_h, l_s, l_v])
    MAX_HSV = numpy.array([u_h, u_s, u_v])

    imageMask = cv2.inRange(image, MIN_HSV, MAX_HSV)
    noBackground = cv2.bitwise_and(image, image, mask=imageMask)
    blurImage = cv2.medianBlur(cv2.GaussianBlur(noBackground, (11, 11), 0), 15)
    # [0] - H, [1] - S, [2] - V
    greyscaleImage = numpy.dsplit(blurImage, blurImage.shape[-1])[2]
    ret, thresh = cv2.threshold(greyscaleImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # display images
    # displayImage(imageMask, '[1] imgMask')
    # displayImage(noBackground, '[2] no BG')
    # displayImage(blurImage, '[3] blurred')
    # displayImage(greyscaleImage, '[4] greyscaled')
    # displayImage(thresh, '[5] thresholded')

    return thresh


# Function to create HSV trackbars
def createHSVTrackBars():
    createNewWindow("HSV Values")
    createTrackbar('L - h', 'HSV Values', 0, 179)
    createTrackbar('U - h', 'HSV Values', 179, 179)
    # Ideal value - 21
    createTrackbar('L - s', 'HSV Values', 0, 255)
    createTrackbar('U - s', 'HSV Values', 255, 255)

    createTrackbar('L - v', 'HSV Values', 0, 255)
    createTrackbar('U - v', 'HSV Values', 255, 255)


# Extracts the region of interest of a image
def extractRegionofInterest(snapshot):
    return snapshot[BOX_Y:BOX_Y + BOX_HEIGHT, BOX_X:BOX_X + BOX_WIDTH]


# Draws a blue rectangle in a image (default: X = 80, Y = 80, WIDTH = 300, HEIGHT = 300)
def drawBoundingRectangle(snapshot, acc=''):
    width = int(BOX_WIDTH / 3)
    height = int(BOX_HEIGHT / 3)
    for i in range(3):
        for j in range(3):
            x = BOX_X + (width * i)
            y = BOX_Y + (height * j)
            snapshot = cv2.rectangle(snapshot, (x, y), (x + width, y + height), (255, 0, 0), 2)
    if type(acc) == type(numpy.float32(0)) and SHOW_ACC:
        cv2.putText(snapshot, str(round(acc*100,2))+"%",
                   (BOX_X, BOX_Y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2,
                   cv2.LINE_AA)
    return snapshot


# Conversts a image from an RGB image to Grayscale
def convertToGrayscale(snapshot):
    return cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
