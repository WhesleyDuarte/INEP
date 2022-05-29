from pandas import DataFrame
from controller.functionsComuns import FunctionsComuns
from controller.educacaoInfantil import EducacaoInfantil
from controller.ensinoFundamental import EnsinoFundamental
from controller.namenateFile import NamenateFile


class FileGenerator:
    def __init__(self) -> None:
        pass

    def generate(self, obj, frame, year):

        self.obj = obj
        self.frame = frame
        self.year = year
        self.newFrame = []
        self.newFrame.append(self.obj.header)

        namingFile = NamenateFile()
        functionComuns = FunctionsComuns()
        educacaoInfantil = EducacaoInfantil()
        ensinoFundamental = EnsinoFundamental()

        for index, linha in self.frame.iterrows():
            if linha["Estado"] == "Mato Grosso do Sul ": #and linha["Municipio"] != "  ":

                if self.obj.sheetName == "Educação Básica 1.1":
                    functionComuns.funcVisaoGeral(linha, self.newFrame, self.obj.index)

                elif self.obj.sheetName == "Creche 1.6":

                    functionComuns.funcUrbana(linha, self.newFrame)
                    functionComuns.funcRural(linha, self.newFrame)

                elif self.obj.sheetName == "1.7":

                    functionComuns.funcFeminina(linha, self.newFrame)
                    functionComuns.funcMasculina(linha, self.newFrame)

                elif self.obj.sheetName == "1.8":

                    educacaoInfantil.funcFaixaEtaria(linha, self.newFrame)

                elif self.obj.sheetName == "Pré-Escola 1.10":

                    functionComuns.funcUrbana(linha, self.newFrame)
                    functionComuns.funcRural(linha, self.newFrame)

                elif self.obj.sheetName == "1.16":

                    functionComuns.funcUrbana(linha, self.newFrame)
                    functionComuns.funcRural(linha, self.newFrame)

        namingFile.namingFile(
            year=self.year,
            tipoEnsinoGrupo=self.obj.tipoEnsinoGrupo,
            nivelTipoEnsino=self.obj.nivelTipoEnsino,
            bodyNameFile=self.obj.bodyNameFile,
            newFrame=self.newFrame,
        )
