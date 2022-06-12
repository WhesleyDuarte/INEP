from view.mat_localizacao import Urbana, Rural
from view.sexoEtnia import Feminina, Masculino
from view.tempoIntegralParcial import TempoParcial, TempoIntegral


class FunctionsComuns(Urbana, Rural, Feminina, Masculino, TempoParcial, TempoIntegral):
    def __init__(self) -> None:
        super().__init__()

    def funcUrbana(self, dado, newDataFrame):

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

    def funcTempoIntegral(self, dado, newDataFrame):
        newDataFrame.append(super().funcTempoIntegralFederal(dado))
        newDataFrame.append(super().funcTempoIntegralEstadual(dado))
        newDataFrame.append(super().funcTempoIntegralMunicipal(dado))
        newDataFrame.append(super().funcTempoIntegralPrivada(dado))

    def funcTempoParcial(self, dado, newDataFrame):
        newDataFrame.append(super().funcTempoParcialFederal(dado))
        newDataFrame.append(super().funcTempoParcialEstadual(dado))
        newDataFrame.append(super().funcTempoParcialMunicipal(dado))
        newDataFrame.append(super().funcTempoParcialPrivada(dado))
