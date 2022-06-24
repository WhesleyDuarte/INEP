from INEP.code.model.abaModel import AbaModel


class Aba(AbaModel):
    def __init__(self, tipoEnsinoGrupo, nivelTipoEnsino, index, skiprows, usecols, bodyNameFile, nameColumns,
                 newColumns, header, sheetName) -> None:
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
