class Feminina:
    def __init__(self) -> None:
        pass

    def funcFemNdeclarado(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sexo_Fem"],
            "Não Declarada",
            format(dado["Fem_Ndeclarado"]).replace(".", ","),
        ]

    def funcFemBranca(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sexo_Fem"],
            "Branca",
            format(dado["Fem_Branca"]).replace(".", ","),
        ]

    def funcFemPreta(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sexo_Fem"],
            "Preta",
            format(dado["Fem_Preta"]).replace(".", ","),
        ]

    def funcFemParda(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sexo_Fem"],
            "Parda",
            format(dado["Fem_Parda"]).replace(".", ","),
        ]

    def funcFemAmarela(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sexo_Fem"],
            "Amarela",
            format(dado["Fem_Amarela"]).replace(".", ","),
        ]

    def funcFemIndigena(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sexo_Fem"],
            "Indígena",
            format(dado["Fem_Indigena"]).replace(".", ","),
        ]


class Masculino:
    def __init__(self) -> None:
        pass

    def funcMascNdeclarado(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sex_Masc"],
            "Não Declarada",
            format(dado["Masc_Ndeclarado"]).replace(".", ","),
        ]

    def funcMascBranca(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sex_Masc"],
            "Branca",
            format(dado["Masc_Branca"]).replace(".", ","),
        ]

    def funcMascPreta(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sex_Masc"],
            "Preta",
            format(dado["Masc_Preta"]).replace(".", ","),
        ]

    def funcMascParda(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sex_Masc"],
            "Parda",
            format(dado["Masc_Parda"]).replace(".", ","),
        ]

    def funcMascAmarela(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sex_Masc"],
            "Amarela",
            format(dado["Masc_Amarela"]).replace(".", ","),
        ]

    def funcMascIndigena(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["Sex_Masc"],
            "Indígena",
            format(dado["Masc_Indigena"]).replace(".", ","),
        ]
