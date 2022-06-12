
class TempoIntegral:
    def __init__(self) -> None:
        pass

    def funcTempoIntegralFederal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoIntegral"],
            dado["DepAdm1"],
            format(dado["IntegralFederal"]).replace(".", ",")
        ]

    def funcTempoIntegralEstadual(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoIntegral"],
            dado["DepAdm2"],
            format(dado["IntegralEstadual"]).replace(".", ","),
        ]

    def funcTempoIntegralMunicipal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoIntegral"],
            dado["DepAdm3"],
            format(dado["IntegralMunicipal"]).replace(".", ","),
        ]

    def funcTempoIntegralPrivada(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoIntegral"],
            dado["DepAdm4"],
            format(dado["IntegralPrivada"]).replace(".", ","),
        ]

class TempoParcial():
    def __init__(self) -> None:
        pass
    
    def funcTempoParcialFederal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoParcial"],
            dado["DepAdm1"],
            format(dado["ParcialFederal"]).replace(".", ","),
        ]

    def funcTempoParcialEstadual(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoParcial"],
            dado["DepAdm2"],
            format(dado["ParcialEstadual"]).replace(".", ","),
        ]

    def funcTempoParcialMunicipal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoParcial"],
            dado["DepAdm3"],
            format(dado["ParcialMunicipal"]).replace(".", ","),
        ]

    def funcTempoParcialPrivada(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["TempoParcial"],
            dado["DepAdm4"],
            format(dado["ParcialPrivada"]).replace(".", ","),
        ]
