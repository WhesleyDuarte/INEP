from .starting import Start


class Main(Start):
    def __init__(self) -> None:
        super().__init__()

    def start(self, obj, startYear, endYear):
        self.startYear = startYear
        self.endYear = endYear
        self.obj = obj
        print(type(self.obj))
        super().starting(obj=self.obj, startYear=self.startYear, endYear=self.endYear)

    def startDimesion(self, obj):
        self.obj = obj
        super().startingDimension(obj=self.obj)
