from view.visaoGeral_educacaoBasica import VisaoGeralEducacaoBasica
from view.visaoGeral_localizacaoDepAdm import VisaoGeralLocalizacaoDepAdministrativa


class VisaoGeral(VisaoGeralEducacaoBasica, VisaoGeralLocalizacaoDepAdministrativa):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def funcVisaoGeralEducacaoBasica(self, dado, newDataFrame, index):
        self.index = index
        self.dado = dado
        newDataFrame.append(super().funcMatriculaTotalEducacaoBasica(dado = self.dado, index = self.index))
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
        
    def funcVisaoGeralLocalizacaoDepAdministrativa(self, dado, newDataFrame, index):
        newDataFrame.append(super().funcMatriculaTotalLocalizacaoDepAdministrativa(dado, self.index))
        newDataFrame.append(super().funcMatriculaUrbanaFederal(dado, self.index))
        newDataFrame.append(super().funcMatriculaUrbanaEstadual(dado, self.index))
        newDataFrame.append(super().funcMatriculaUrbanaMunicipal(dado, self.index))
        newDataFrame.append(super().funcMatriculaUrbanaPrivada(dado, self.index))
        newDataFrame.append(super().funcMatriculaRuralFederal(dado, self.index))
        newDataFrame.append(super().funcMatriculaRuralEstadual(dado, self.index))
        newDataFrame.append(super().funcMatriculaRuralMunicipal(dado, self.index))
        newDataFrame.append(super().funcMatriculaRuralPrivada(dado, self.index))
        
         