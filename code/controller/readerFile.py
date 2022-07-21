import pandas as pd
import os


class ReaderFile:
    def __init__(self) -> None:
        pass

    def searchFile(self, nameFileSheet):
        self.nameFileSheet = nameFileSheet

        for file in os.listdir("./arquivosExcel"):
            if file.endswith(self.nameFileSheet):
                return os.path.join(
                    os.path.realpath("./arquivosExcel/"), file
                )

    def read(self, frame, sheetName, pathFile, nameFileSheet):

        self.frame = frame
        self.sheetName = sheetName
        self.pathAbsolute = pathFile
        self.nameFileSheet = nameFileSheet

        '''sheetName,  nameFileSheet, pathFile, skiprows=None, usecols=None, '''

        if "Skiprows" and "Usecols" in self.frame:
            return pd.read_excel(
                self.pathAbsolute,
                sheet_name=self.sheetName,
                skiprows=self.frame["Skiprows"],
                usecols=self.frame["Usecols"],
            )
        else:
            return pd.read_excel(
                self.pathAbsolute,
                sheet_name=self.sheetName,
                skiprows=None,
                usecols=None,
            )

        '''
        self.usecols = self.frame["Usecols"]
        self.sheetName = self.frame["SheetName"]

        self.nameFileSheet = self.frame["NameFileSheet"]
        self.pathAbsolute = self.frame["PathFile"]
        '''
        print("Reader File...")

        return pd.read_excel(
            self.pathAbsolute,
            sheet_name=self.sheetName,
            skiprows=self.skiprows,
            usecols=self.usecols,
        )


