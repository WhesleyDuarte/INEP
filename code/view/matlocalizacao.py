class Urbana:
    def __init__(self) -> None:
        pass

    def funcUrbanaFederal(self, dado):

        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoUrb"],
            dado["DepAdm1"],
            format(dado["UrbFederal"]).replace(".", ",")
        ]


    def funcUrbanaEstadual(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoUrb"],
            dado["DepAdm2"],
            format(dado["UrbEstadual"]).replace(".", ","),
        ]

    def funcUrbanaMunicipal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoUrb"],
            dado["DepAdm3"],
            format(dado["UrbMunicipal"]).replace(".", ","),
        ]

    def funcUrbanaPrivada(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoUrb"],
            dado["DepAdm4"],
            format(dado["UrbPrivada"]).replace(".", ","),
        ]


class Rural:
    def __init__(self) -> None:
        pass

    def funcRuralFederal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoRural"],
            dado["DepAdm1"],
            format(dado["RuralFederal"]).replace(".", ","),
        ]

    def funcRuralEstadual(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoRural"],
            dado["DepAdm2"],
            format(dado["RuralEstadual"]).replace(".", ","),
        ]

    def funcRuralMunicipal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoRural"],
            dado["DepAdm3"],
            format(dado["RuralMunicipal"]).replace(".", ","),
        ]

    def funcRuralPrivada(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["LocalizacaoRural"],
            dado["DepAdm4"],
            format(dado["RuralPrivada"]).replace(".", ","),
        ]
