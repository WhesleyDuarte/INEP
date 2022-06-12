from view.faixaEtaria_educacaoInfantil import FaixaEtariaEducacaoInfantil


class EducacaoInfantil(FaixaEtariaEducacaoInfantil):
    def __init__(self) -> None:
        super().__init__()

    def funcFaixaEtaria(self, dado, newDataFrame):
        newDataFrame.append(super().funcAte3Anos(dado))
        newDataFrame.append(super().func4a5Anos(dado))
        newDataFrame.append(super().func6Anos(dado))
