class Urbana:
    def __init__(self) -> None:
        pass

    def funcUrbanaFederal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Urb"],
            "Federal",
            format(dado["Urb_Federal"]).replace(".", ","),
        ]

    def funcUrbanaEstadual(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Urb"],
            "Estadual",
            format(dado["Urb_Estadual"]).replace(".", ","),
        ]

    def funcUrbanaMunicipal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Urb"],
            "Municipal",
            format(dado["Urb_Municipal"]).replace(".", ","),
        ]

    def funcUrbanaPrivada(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Urb"],
            "Privada",
            format(dado["Urb_Privada"]).replace(".", ","),
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
            dado["Localizacao_Rural"],
            "Federal",
            format(dado["Rural_Federal"]).replace(".", ","),
        ]

    def funcRuralEstadual(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Rural"],
            "Estadual",
            format(dado["Rural_Estadual"]).replace(".", ","),
        ]

    def funcRuralMunicipal(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Rural"],
            "Municipal",
            format(dado["Rural_Municipal"]).replace(".", ","),
        ]

    def funcRuralPrivada(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Localizacao_Rural"],
            "Privada",
            format(dado["Rural_Privada"]).replace(".", ","),
        ]
