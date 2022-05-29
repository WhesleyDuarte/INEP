class Aba:
    def __init__(self, dataSheet) -> None:

        self.obj = dataSheet
        self.sheetName = self.obj["sheetName"]
        self.index = self.obj["index"]
