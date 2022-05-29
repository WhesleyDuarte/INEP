import pandas as pd
import os


class ReaderFile:
    def __init__(self) -> None:
        pass

    def searchFile(self, nameFileSheet):
        self.nameFileSheet = nameFileSheet

        for file in os.listdir("./codigo_supai_refatorado/arquivosExcel"):
            if file.endswith(self.nameFileSheet):
                return os.path.join(
                    os.path.realpath("./codigo_supai_refatorado/arquivosExcel/"), file
                )

    def read(self, sheetName, skiprows, usecols, nameFileSheet, pathFile):

        self.sheetName = sheetName
        self.skiprows = skiprows
        self.usecols = usecols
        self.nameFileSheet = nameFileSheet
        self.pathAbsolute = pathFile

        print("Reader File...")

        return pd.read_excel(
            self.pathAbsolute,
            sheet_name=self.sheetName,
            skiprows=self.skiprows,
            usecols=self.usecols,
        )
