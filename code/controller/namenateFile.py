import unidecode
from .salveFile import SalveFile


class NamenateFile:
    def __init__(self) -> None:
        pass

    def namingFile(
        self,
        year,
        tipoEnsinoGrupo,
        nivelTipoEnsino,
        bodyNameFile,
        newFrame,
    ):
        self.year = year
        self.tipoEnsinoGrupo = tipoEnsinoGrupo
        self.nivelTipoEnsino = nivelTipoEnsino
        self.bodyNameFile = bodyNameFile
        self.newFrame = newFrame

        saveFile = SalveFile()

        if self.tipoEnsinoGrupo == self.nivelTipoEnsino:
            fileNameCSV = unidecode.unidecode(
                f"{self.year}{self.bodyNameFile}{self.tipoEnsinoGrupo}.csv".replace(
                    " ", ""
                )
            )
        else:
            fileNameCSV = unidecode.unidecode(
                f"{self.year}{self.bodyNameFile}{self.tipoEnsinoGrupo}_{self.nivelTipoEnsino}.csv".replace(
                    " ", ""
                )
            )
        saveFile.savingFile(fileNameCSV=fileNameCSV, newFrame=self.newFrame)

    def namingFileDimension(self, sheetName, newDimensao):
        saveFile = SalveFile()
        self.fileNameCSV = sheetName
        self.newFrame = newDimensao

        self.fileNameCSV = unidecode.unidecode(
            f"{self.fileNameCSV}.csv".replace(
                " ", ""
            )
        )
        saveFile.savingFile(fileNameCSV=self.fileNameCSV, newFrame=newDimensao)