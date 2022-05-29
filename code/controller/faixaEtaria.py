class FaixaEtaria:
    def __init__(self) -> None:
        pass

    def funcAte3Anos(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["FaixaEtaria"],
            format(dado["Até 3 Anos"]).replace(".", ","),
        ]

    def func4a5Anos(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["FaixaEtaria2"],
            format(dado["4 a 5 Anos"]).replace(".", ","),
        ]

    def func6Anos(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["FaixaEtaria3"],
            format(dado["6 Anos ou mais"]).replace(".", ","),
        ]

    def funcAte5Anos(self, dado):
        return [
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["tipoEnsinoGrupo"],
            dado["nivelTipoEnsino"],
            dado["FaixaEtaria3"],
            format(dado["6 Anos ou mais"]).replace(".", ","),
        ]
