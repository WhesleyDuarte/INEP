
import imp
from view.faixaEtaria_ensinoFundamental import FaixaEtariaEnsinoFuncamental
from view.anoDepAdministrativa_ensinoFundamental import AnosIniciais


class EnsinoFundamental(FaixaEtariaEnsinoFuncamental, AnosIniciais):
    def __init__(self) -> None:
        super().__init__()

    def funcFaixaEtaria(self, dado, newDataFrame):
    
        newDataFrame.append(super().funcAte5Anos(dado))
        newDataFrame.append(super().func6Ate10Anos(dado))
        newDataFrame.append(super().func11Ate14Anos(dado))
        newDataFrame.append(super().func15Ate17Anos(dado))
        newDataFrame.append(super().func18Ate20Anos(dado))
        newDataFrame.append(super().func20OuMais(dado))
        
    def funcAnosIniciais(self, dado, newDataFrame):
        newDataFrame.append(super().primeiroAnoFederal(dado))
        newDataFrame.append(super().primeiroAnoEstadual(dado))
        newDataFrame.append(super().primeiroAnoMunicipal(dado))
        newDataFrame.append(super().primeiroAnoPrivada(dado))
        newDataFrame.append(super().segundoAnoFederal(dado))
        newDataFrame.append(super().segundoAnoEstadual(dado))
        newDataFrame.append(super().segundoAnoMunicipal(dado))
        newDataFrame.append(super().segundoAnoPrivada(dado))
        newDataFrame.append(super().terceiroAnoFederal(dado))
        newDataFrame.append(super().terceiroAnoEstadual(dado))
        newDataFrame.append(super().terceiroAnoMunicipal(dado))
        newDataFrame.append(super().terceiroAnoPrivada(dado))
        newDataFrame.append(super().quartoAnoFederal(dado))
        newDataFrame.append(super().quartoAnoEstadual(dado))
        newDataFrame.append(super().quartoAnoMunicipal(dado))
        newDataFrame.append(super().quartoAnoPrivada(dado))
        newDataFrame.append(super().quintoAnoFederal(dado))
        newDataFrame.append(super().quintoAnoEstadual(dado))
        newDataFrame.append(super().quintoAnoMunicipal(dado))
        newDataFrame.append(super().quintoAnoPrivada(dado))
