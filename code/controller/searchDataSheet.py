import json
import os
from unicodedata import name


class SearchDataSheet:
    def __init__(self) -> None:
       pass

    def searchingNameSheet(self,  nameSheet, nameFileJason):
        self.nameSheet = nameSheet
        self.nameFileJason = nameFileJason 
        
        for file in os.listdir("./arquivosExcel"):
            if file.endswith(self.nameFileJason):
                with open(
                    os.path.join(
                        os.path.realpath("./arquivosExcel/"),
                        file,
                    ),
                    encoding="utf-8",
                ) as fileJson:
                    #self.dataAllSheet = json.load(fileJson)
                    #return self.dataAllSheet
                    return json.load(fileJson)

    def searchingDataSheet(self, dataSheet):
        self.dataSheet = dataSheet
        for sheet in self.dataSheet:
            if sheet == self.nameSheet:
                return self.dataSheet[sheet]
