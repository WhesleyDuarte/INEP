from .namenateFile import NamenateFile


class BuildDimension():
    def __init__(self):
        pass

    def buildingDimension(self, obj):
        newDimensao = []
        newDimensao.append(getattr(obj, "header"))
        sk = 0
        for index in range(len(getattr(self.obj, "dimensao"))):
            sk = sk + 1
            newDimensao.append([sk, getattr(self.obj, "dimensao")[index]])
        return newDimensao
