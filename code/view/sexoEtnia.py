class Feminina:
    def __init__(self) -> None:
        pass

    def funcFemNdeclarado(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexoFem"],
            "Não Declarada",
            format(dado["FemNdeclarado"]).replace(".", ","),
        ]

    def funcFemBranca(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexoFem"],
            "Branca",
            format(dado["FemBranca"]).replace(".", ","),
        ]

    def funcFemPreta(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexoFem"],
            "Preta",
            format(dado["FemPreta"]).replace(".", ","),
        ]

    def funcFemParda(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexoFem"],
            "Parda",
            format(dado["FemParda"]).replace(".", ","),
        ]

    def funcFemAmarela(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexoFem"],
            "Amarela",
            format(dado["FemAmarela"]).replace(".", ","),
        ]

    def funcFemIndigena(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexoFem"],
            "Indígena",
            format(dado["FemIndigena"]).replace(".", ","),
        ]


class Masculino:
    def __init__(self) -> None:
        pass

    def funcMascNdeclarado(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexMasc"],
            "Não Declarada",
            format(dado["MascNdeclarado"]).replace(".", ","),
        ]

    def funcMascBranca(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexMasc"],
            "Branca",
            format(dado["MascBranca"]).replace(".", ","),
        ]

    def funcMascPreta(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexMasc"],
            "Preta",
            format(dado["MascPreta"]).replace(".", ","),
        ]

    def funcMascParda(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexMasc"],
            "Parda",
            format(dado["MascParda"]).replace(".", ","),
        ]

    def funcMascAmarela(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexMasc"],
            "Amarela",
            format(dado["MascAmarela"]).replace(".", ","),
        ]

    def funcMascIndigena(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["SexMasc"],
            "Indígena",
            format(dado["MascIndigena"]).replace(".", ","),
        ]
