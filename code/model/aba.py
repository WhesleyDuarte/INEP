

class Aba:
    def __init__(self, dataSheet) -> None:

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
