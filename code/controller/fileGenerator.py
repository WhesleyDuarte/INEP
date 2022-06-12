from pandas import DataFrame
from controller.functionsComuns import FunctionsComuns
from controller.educacaoInfantil import EducacaoInfantil
from controller.ensinoFundamental import EnsinoFundamental
from controller.namenateFile import NamenateFile
from controller.visaoGeral import VisaoGeral


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
        visaoGeral = VisaoGeral()

        for index, linha in self.frame.iterrows():
            if linha["Estado"] == "Mato Grosso do Sul " and linha["Municipio"] != "  ":

                if self.obj.sheetName == "Creche 1.6":
                    functionComuns.funcUrbana(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcRural(dado=linha, newDataFrame=self.newFrame)

                elif self.obj.sheetName == "1.7":

                    functionComuns.funcFeminina(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcMasculina(dado=linha, newDataFrame=self.newFrame)

                elif self.obj.sheetName == "1.8":
                    educacaoInfantil.funcFaixaEtaria(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "1.9":
                    functionComuns.funcTempoIntegral(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcTempoParcial(dado=linha, newDataFrame=self.newFrame)

                elif self.obj.sheetName == "Pré-Escola 1.10":
                    functionComuns.funcUrbana(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcRural(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "1.11":
                    functionComuns.funcFeminina(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcMasculina(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "1.12":
                    educacaoInfantil.funcFaixaEtaria(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "1.13":
                    functionComuns.funcTempoIntegral(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcTempoParcial(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "Anos Iniciais 1.15":
                    ensinoFundamental.funcAnosIniciais(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "1.16":
                    functionComuns.funcUrbana(dado=linha, newDataFrame=self.newFrame)
                    functionComuns.funcRural(dado=linha, newDataFrame=self.newFrame)
                
                elif self.obj.sheetName == "1.18":
                    ensinoFundamental.funcFaixaEtaria()
                    
            elif linha["Estado"] == "Mato Grosso do Sul " and linha["Municipio"] == "  ":
                if self.obj.sheetName == "Educação Básica 1.1":
                    visaoGeral.funcVisaoGeralEducacaoBasica(dado=linha, newDataFrame=self.newFrame, index=self.obj.index)
                
                elif self.obj.sheetName == "1.2":
                    visaoGeral.funcVisaoGeralLocalizacaoDepAdministrativa(dado=linha, newDataFrame=self.newFrame, index=self.obj.index)
                    
        namingFile.namingFile(
            year=self.year,
            tipoEnsinoGrupo=self.obj.tipoEnsinoGrupo,
            nivelTipoEnsino=self.obj.nivelTipoEnsino,
            bodyNameFile=self.obj.bodyNameFile,
            newFrame=self.newFrame,
        )
