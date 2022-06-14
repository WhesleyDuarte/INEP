
from INEP.code.model.abaModel import AbaModel


class Aba(AbaModel):
    def __init__(self, tipoEnsinoGrupo, nivelTipoEnsino, index, skiprows, usecols, bodyNameFile, nameColumns,
                 newColumns, header, sheetName) -> None:
        super().__init__(sheetName)
        """ 
        self.obj = dataSheet
        self.sheetName = self.obj["SheetName"]
        self.tipoEnsinoGrupo = self.obj["TipoEnsinoGrupo"]
        self.nivelTipoEnsino = self.obj["NivelTipoEnsino"]
        self.index = self.obj["Index"]
        self.skiprows = self.obj["Skiprows"]
        self.usecols = self.obj["Usecols"]
        self.bodyNameFile = self.obj["BodyNameFile"]
        self.nameColumns = self.obj["NameColumns"]
        self.newColumns = self.obj["NewColumns"]
        self.header = self.obj["Header"]
        """
        # self.obj = dataSheet
        # self.sheetName = self.obj["SheetName"]
        self.tipoEnsinoGrupo = tipoEnsinoGrupo
        self.nivelTipoEnsino = nivelTipoEnsino
        self.index = index
        self.skiprows = skiprows
        self.usecols = usecols
        self.bodyNameFile = bodyNameFile
        self.nameColumns = nameColumns
        self.newColumns = newColumns
        self.header = header
