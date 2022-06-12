class AbaModel:
    def __init__(self, dataSheet) -> None:

        self.obj = dataSheet
        self.sheetName = self.obj["SheetName"]
        
