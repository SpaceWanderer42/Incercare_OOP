import math
# lalala
class Point:
    x = 0.0
    y = 0.0
    z = 0.0
    containsAzimuth = True

    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    #     z = 0.0
    #     containsAzimuth = False

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z


    def radToDeg(self, val):

        self.val = val*180/math.pi

        if(self.val < 0):

                self.val = self.val + 360
                return self.val
        else: return self.val


    def getX(self):

        return self.x

    def getY(self):

        return self.y

    def getZ(self):

        return self.z

    def getRadius(self):

        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    # def getRadius(self, a):
    #
    #     return a

    def getPhi(self):

        return self.radToDeg(math.atan2(self.x, self.y))

    def getTheta(self):

        if(Point.containsAzimuth):
            return self.radToDeg((math.atan2(math.sqrt(self.x * self.x + self.y + self.y))))
        return 0




