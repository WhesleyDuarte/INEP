from .mat_localizacao import Urbana, Rural
from .sexoEtnia import Feminina, Masculino
from .visaoGeral import VisaoGeral


class FunctionsComuns(Urbana, Rural, Feminina, Masculino, VisaoGeral):
    def __init__(self) -> None:
        super().__init__()

    def funcUrbana(self, dado, newDataFrame ):
   
        newDataFrame.append(super().funcUrbanaFederal(dado))
        newDataFrame.append(super().funcUrbanaEstadual(dado))
        newDataFrame.append(super().funcUrbanaMunicipal(dado))
        newDataFrame.append(super().funcUrbanaPrivada(dado))

    def funcRural(self, dado, newDataFrame):

        newDataFrame.append(super().funcRuralFederal(dado))
        newDataFrame.append(super().funcRuralEstadual(dado))
        newDataFrame.append(super().funcRuralMunicipal(dado))
        newDataFrame.append(super().funcRuralPrivada(dado))

    def funcFeminina(self, dado, newDataFrame):

        newDataFrame.append(super().funcFemNdeclarado(dado))
        newDataFrame.append(super().funcFemBranca(dado))
        newDataFrame.append(super().funcFemPreta(dado))
        newDataFrame.append(super().funcFemParda(dado))
        newDataFrame.append(super().funcFemAmarela(dado))
        newDataFrame.append(super().funcFemIndigena(dado))

    def funcMasculina(self, dado, newDataFrame):

        newDataFrame.append(super().funcMascNdeclarado(dado))
        newDataFrame.append(super().funcMascBranca(dado))
        newDataFrame.append(super().funcMascPreta(dado))
        newDataFrame.append(super().funcMascParda(dado))
        newDataFrame.append(super().funcMascAmarela(dado))
        newDataFrame.append(super().funcMascIndigena(dado))

    def funcVisaoGeral(self, dado, newDataFrame, index):
        self.index = index
        newDataFrame.append(super().funcMatriculaTotal(dado, self.index))
        newDataFrame.append(super().funcMatriculaCreche(dado, self.index))
        newDataFrame.append(super().funcMatriculaPreEscola(dado, self.index))
        newDataFrame.append(super().funcMatriculaAnosIniciais(dado, self.index))
        newDataFrame.append(super().funcMatriculaAnosFinais(dado, self.index))
        newDataFrame.append(
            super().funcMatriculaEnsinoMedioPropedeutico(dado, self.index)
        )
        newDataFrame.append(super().funcMatriculaEnsinoMedioNormal(dado, self.index))
        newDataFrame.append(super().funcMatriculaEnsinoMedioIntegrado(dado, self.index))
        newDataFrame.append(
            super().funcMatriculaProfissionalAssociado(dado, self.index)
        )
        newDataFrame.append(
            super().funcMatriculaProfissionalConcomitante(dado, self.index)
        )
        newDataFrame.append(
            super().funcMatriculaProfissionalSubsequente(dado, self.index)
        )
        newDataFrame.append(super().funcMatriculaFICConcomitante(dado, self.index))
        newDataFrame.append(super().funcMatriculaFICIntegrado(dado, self.index))
        newDataFrame.append(super().funcMatriculaEJAFundamental(dado, self.index))
        newDataFrame.append(super().funcMatriculaEJAMedio(dado, self.index))
        newDataFrame.append(super().funcMatriculaEspecialComum(dado, self.index))
        newDataFrame.append(super().funcMatriculaEspecialExclusiva(dado, self.index))
