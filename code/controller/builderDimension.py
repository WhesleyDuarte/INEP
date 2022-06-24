from .namenateFile import NamenateFile


class BuildDimension():
    def __init__(self):
        pass

    def buildingDimension(self, obj):
        newDimensao = []
        newDimensao.append(getattr(obj, "header"))
        count = 0
        for sk in range(len(getattr(self.obj, "dimensao"))):
            count = count + 1
            newDimensao.append([count, getattr(self.obj, "dimensao")[sk]])
        return newDimensao
