import numpy as np


class SalveFile:
    def __init__(self) -> None:
        pass

    def savingFile(self, fileNameCSV, newFrame):
        self.newFrame = newFrame
        self.fileNameCSV = fileNameCSV

        np.savetxt(
            self.fileNameCSV, self.newFrame, delimiter=";", fmt="%s", encoding="utf-8"
        )
        print(f"Arquivo: {self.fileNameCSV} gerado com Sucesso!!!")
