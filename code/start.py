from ast import Not

from controller.main import Main
from controller.searchDataSheet import SearchDataSheet
from model.aba import Aba


class Instances(SearchDataSheet):
    def __init__(self, nameSheet, startYear, endYear, fileJson) -> None:
        super().__init__()

        self.nameSheet = nameSheet
        self.startYear = startYear
        self.endYear = endYear
        self.fileJson = fileJson

        pass

    def validating(self):
        # TODO: vamos criar a instência de cada tipo de obejto, exemplo abas e notas

        if self.fileJson == "planilha.json":
            pass
        else:
            dataSheet = super().searchingNameSheet(self.nameSheet, self.fileJson)
            obj = super().searchingDataSheet(dataSheet)
            objAba = Aba(sheetName=obj["SheetName"], nameColumns=obj["NameColumns"],
                         tipoEnsinoGrupo=obj["TipoEnsinoGrupo"], nivelTipoEnsino=obj["NivelTipoEnsino"],
                         index=obj["Index"], skiprows=obj["Skiprows"], newColumns=obj["NewColumns"],
                         bodyNameFile=obj["BodyNameFile"], usecols=obj["Usecols"], header=obj["Header"])

            main = Main()
            main.start(objAba, self.startYear, self.endYear)


dadosAbas = "dadosAbas.json"
planilha = "planilha.json"

startYear = 2013
endYear = 2014
nameSheet = "Pré-Escola 1.10"
fileJson = dadosAbas

starter = Instances(
    nameSheet=nameSheet, startYear=startYear, endYear=endYear, fileJson=fileJson
)
starter.validating()

"""
[
    "Educação Básica 1.1", OK
    "1.2",
    "1.3",
    "1.4",
    "Educação Infantil 1.5",
    "Creche 1.6", OK
    "1.7",OK
    "1.8", OK
    "1.9", OK
    "Pré-Escola 1.10", OK
    "1.11", OK
    "1.12",  OK
    "1.13", OK
    "Ensino Fundamental 1.14",
    "Anos Iniciais 1.15",
    "1.16",
    "1.17",
    "1.18",
    "1.19",
    "Anos Finais 1.20",
    "1.21",
    "1.22",
    "1.23",
    "1.24",
    "Ensino Médio 1.25",
    "1.26",
    "1.27",
    "1.28",
    "1.29",
    "Educação Profissional 1.30",
    "1.31",
    "1.32",
    "1.33",
    "EJA 1.34",
    "1.35",
    "1.36",
    "1.37",
    "Educação Especial 1.38",
    "Classes Comuns 1.39",
    "1.40",
    "1.41",
    "1.42",
    "1.43",
    "1.44",
    "Classes Exclusivas 1.45",
    "1.46",
    "1.47",
    "1.48",
    "1.49",
    "1.50",
]
"""
