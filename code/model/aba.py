class Aba:
    def __init__(self, dataSheet) -> None:

        self.obj = dataSheet
        self.sheetName = self.obj["sheetName"]
        self.tipoEnsinoGrupo = self.obj["tipoEnsinoGrupo"]
        self.nivelTipoEnsino = self.obj["nivelTipoEnsino"]
        self.index = self.obj["index"]
        self.skiprows = self.obj["skiprows"]
        self.usecols = self.obj["usecols"]
        self.bodyNameFile = self.obj["bodyNameFile"]
        self.nameColumns = self.obj["nameColumns"]
        self.newColumns = self.obj["newColumns"]
        self.header = self.obj["header"]
