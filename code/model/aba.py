from INEP.code.model.abaModel import AbaModel

'''
class Aba(AbaModel):
    def __init__(self, tipoEnsinoGrupo, nivelTipoEnsino, index, bodyNameFile, nameColumns,
                 newColumns, header, sheetName, skiprows=None, usecols=None) -> None:
        super().__init__(sheetName, header)
        
        self.tipoEnsinoGrupo = tipoEnsinoGrupo
        self.nivelTipoEnsino = nivelTipoEnsino
        self.index = index
        self.skiprows = skiprows
        self.usecols = usecols
        self.bodyNameFile = bodyNameFile
        self.nameColumns = nameColumns
        self.newColumns = newColumns
        self.header = header
'''

class Aba():
    def __init__(self, aba):
        self.aba = aba

        #todo: verificar como deixar parâmetros como não obrigatório
        self.sheetName = self.aba["SheetName"]
        self.tipoEnsinoGrupo = self.aba["TipoEnsinoGrupo"]
        self.nivelTipoEnsino = self.aba["NivelTipoEnsino"]
        self.index = self.aba["Index"]
        self.skiprows = self.aba["Skiprows"]
        self.usecols = self.aba["Usecols"]
        self.bodyNameFile = self.aba["BodyNameFile"]
        self.nameColumns = self.aba["NameColumns"]
        self.newColumns = self.aba["NewColumns"]
        self.header = self.aba["Header"]