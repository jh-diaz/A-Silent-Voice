import cv2
import os


# Class to record images and videos and saves them to a given save location
class Recorder:
    def __init__(self, width, height, saveLocation="", frameName=''):
        self.dir = [saveLocation, saveLocation + "/frames/", saveLocation + "/frames/rgb/",
                    saveLocation + "/frames/greyscale/", saveLocation + "/frames/processed/"]
        for i in range(26):
            self.dir.append(os.path.dirname(self.dir[2] + chr(i + 65) + "/"))
            self.dir.append(os.path.dirname(self.dir[3] + chr(i + 65) + "/"))
            self.dir.append(os.path.dirname(self.dir[4] + chr(i + 65) + "/"))

        self.__checkSaveLocation__(self.dir)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(saveLocation + "/" + 'output.mp4', fourcc, 20.0, (width, height))
        self.saveLoc = saveLocation
        self.frameName = frameName
        self.frameCountRGB = 0
        self.frameCountGREY = 0
        self.frameCountBW = 0

    # Save image starting count
    def countStart(self, count):
        self.frameCountRGB = count
        self.frameCountGREY = count
        self.frameCountBW = count

    # Checks if the save location exists
    # Creates it if it does not exist
    def __checkSaveLocation__(self, dir):
        for i in dir:
            if not os.path.exists(i):
                print(i)
                os.mkdir(i)

    # Appens an image to the video that is being recorded
    def recordFrame(self, frame):
        self.out.write(frame)

    # Saves the frame to the save location
    # Saves an RGB, Processed and Grayscale image
    def saveFrame(self, frame, type='RGB', letter=65):
        frame = cv2.resize(frame, (150, 150))
        if type == 'RGB':
            cv2.imwrite(self.dir[5 + (letter - 65) * 3] + "/" + self.frameName + str(self.frameCountRGB) + ".jpg",
                        frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            self.frameCountRGB += 1
        if type == 'BW':
            cv2.imwrite(self.dir[7 + (letter - 65) * 3] + "/" + self.frameName + str(self.frameCountGREY) + ".jpg",
                        frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            self.frameCountGREY += 1
        if type == 'GREY':
            cv2.imwrite(self.dir[6 + (letter - 65) * 3] + "/" + self.frameName + str(self.frameCountBW) + ".jpg", frame,
                        [cv2.IMWRITE_JPEG_QUALITY, 100])
            self.frameCountBW += 1

    # Closes the video recorder when recording a video is finished
    def onDone(self):
        self.out.release()
