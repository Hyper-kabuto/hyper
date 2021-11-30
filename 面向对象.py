'''
水杯
属性(变量)：高度，容积，颜色，材质
行为(方法)：能存放液体

'''
class water_cup:
    __high = 0.0
    color = ""
    __volume = 0
    __material = ""

    def setHigh(self,high):
        if high > 50 or high < 10:
            print("no")
        else:
            self.__high = high
    def getHigh(self):
        return self.__high

    def setVolume(self,volume):
        if volume < 0 or volume > 2000:
            print("no")
        else:
            self.__volume = volume
    def getVolume(self):
        return self.__volume

    def setMaterial(self,material):
        if material != "pp" and material != "po":
            print("no")
        else:
            self.__material = material
    def getMaterial(self):
        return self.__material


    def store(self):
        print("水杯介绍："
              "高度(cm)：",self.__high,
              "容积(ml)：",self.__volume,
              "颜色：",self.color,
              "材料",self.__material)

cup = water_cup()

cup.setHigh(25)
cup.color = "银，绿，黄"
cup.setVolume(580)
cup.setMaterial("pp")

cup.store()










