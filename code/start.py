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

        """
        vamos criar a instência de cada tipo de obejto, exemplo abas e notas
        """
        if self.fileJson == "planilha.json":
            pass
        else:
            dataSheet = super().searchingNameSheet(self.nameSheet, self.fileJson)
            objAba = Aba(super().searchingDataSheet(dataSheet))

            main = Main()
            main.start(objAba, self.startYear, self.endYear)


dadosAbas = "dadosAbas.json"
planilha = "planilha.json"

startYear = 2011
endYear = 2012
nameSheet = "Educação Básica 1.1"
fileJson = dadosAbas


starter = Instances(
    nameSheet=nameSheet, startYear=startYear, endYear=endYear, fileJson=fileJson
)
starter.validating()


"""
[
    "Educação Básica 1.1",
    "1.2",
    "1.3",
    "1.4",
    "Educação Infantil 1.5",
    "Creche 1.6",
    "1.7",
    "1.8",
    "1.9",
    "Pré-Escola 1.10",
    "1.11",
    "1.12",
    "1.13",
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
