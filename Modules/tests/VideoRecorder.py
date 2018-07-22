import cv2
import os

class Recorder:
    def __init__(self, width, height, saveLocation="", frameName=''):
        self.dir = [saveLocation, saveLocation+"/frames/"]
        for i in range(27):
            if i == 26:
                self.dir.append(os.path.dirname(self.dir[1] + "ily/"))
                self.dir.append(os.path.dirname(self.dir[1] + "ily"+"/processed/"))
                self.dir.append(os.path.dirname(self.dir[1] + "ily"+"/greyscale/"))
            else:
                self.dir.append(os.path.dirname(self.dir[1] + chr(i + 65)+"/"))
                self.dir.append(os.path.dirname(self.dir[1] + chr(i + 65)+"/processed/"))
                self.dir.append(os.path.dirname(self.dir[1] + chr(i + 65)+"/greyscale/"))

        self.__checkSaveLocation__(self.dir)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(saveLocation+"/"+'output.mp4', fourcc, 20.0, (width, height))
        self.saveLoc = saveLocation
        self.frameName = frameName
        self.frameCountRGB = 0
        self.frameCountGREY = 0
        self.frameCountBW = 0

    def countStart(self, count):
        self.frameCountRGB = count
        self.frameCountGREY = count
        self.frameCountBW = count

    def __checkSaveLocation__(self, dir):
        for i in dir:
            print(i)
            if not os.path.exists(i):
                os.mkdir(i)

    def recordFrame(self, frame):
        self.out.write(frame)

    def saveFrame(self, frame, type='RGB', letter=65):
        frame = cv2.resize(frame, (50, 50))
        if type=='RGB':
            cv2.imwrite(self.dir[2+(letter-65)*3]+"/"+self.frameName+str(self.frameCountRGB)+".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            self.frameCountRGB +=1
        if type=='BW':
            cv2.imwrite(self.dir[3+(letter-65)*3]+"/"+self.frameName+str(self.frameCountGREY)+".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            self.frameCountGREY +=1
        if type=='GREY':
            cv2.imwrite(self.dir[4+(letter-65)*3]+"/"+self.frameName+str(self.frameCountBW)+".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            self.frameCountBW +=1

    def onDone(self):
        self.out.release()



