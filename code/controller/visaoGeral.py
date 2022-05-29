class VisaoGeral:
    def __init__(self) -> None:
        pass

    def funcMatriculaTotal(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                "00",
                format(dado["qtdMatriculasTotal"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                "00",
                format(dado["qtdMatriculasTotal"]).replace(".", ","),
            ]

    def funcMatriculaCreche(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[0]}" f"{self.index[0]}",
                format(dado["qtdMatriculasCreche"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[0]}" f"{self.index[0]}",
                format(dado["qtdMatriculasCreche"]).replace(".", ","),
            ]

    def funcMatriculaPreEscola(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[0]}" f"{self.index[1]}",
                format(dado["qtdMatriculasPreEscola"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[0]}" f"{self.index[1]}",
                format(dado["qtdMatriculasPreEscola"]).replace(".", ","),
            ]

    def funcMatriculaAnosIniciais(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[1]}" f"{self.index[0]}",
                format(dado["qtdMatriculasAnosIniciais"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[1]}" f"{self.index[0]}",
                format(dado["qtdMatriculasAnosIniciais"]).replace(".", ","),
            ]

    def funcMatriculaAnosFinais(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[1]}" f"{self.index[1]}",
                format(dado["qtdMatriculasAnosFinais"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[1]}" f"{self.index[1]}",
                format(dado["qtdMatriculasAnosFinais"]).replace(".", ","),
            ]

    def funcMatriculaEnsinoMedioPropedeutico(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[2]}" f"{self.index[0]}",
                format(dado["qtdMatriculasEnsinoMedioPropedeutico"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[2]}" f"{self.index[0]}",
                format(dado["qtdMatriculasEnsinoMedioPropedeutico"]).replace(".", ","),
            ]

    def funcMatriculaEnsinoMedioNormal(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[2]}" f"{self.index[1]}",
                format(dado["qtdMatriculasEnsinoMedioNormal"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[2]}" f"{self.index[1]}",
                format(dado["qtdMatriculasEnsinoMedioNormal"]).replace(".", ","),
            ]

    def funcMatriculaEnsinoMedioIntegrado(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[2]}" f"{self.index[2]}",
                format(dado["qtdMatriculasEnsinoMedioIntegrado"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[2]}" f"{self.index[2]}",
                format(dado["qtdMatriculasEnsinoMedioIntegrado"]).replace(".", ","),
            ]

    def funcMatriculaProfissionalAssociado(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[3]}" f"{self.index[0]}",
                format(dado["qtdMatriculasProfissionalAssociado"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[3]}" f"{self.index[0]}",
                format(dado["qtdMatriculasProfissionalAssociado"]).replace(".", ","),
            ]

    def funcMatriculaProfissionalConcomitante(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[3]}" f"{self.index[1]}",
                format(dado["qtdMatriculasProfissionalConcomitante"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[3]}" f"{self.index[1]}",
                format(dado["qtdMatriculasProfissionalConcomitante"]).replace(".", ","),
            ]

    def funcMatriculaProfissionalSubsequente(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[3]}" f"{self.index[2]}",
                format(dado["qtdMatriculasProfissionalSubsequente"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[3]}" f"{self.index[2]}",
                format(dado["qtdMatriculasProfissionalSubsequente"]).replace(".", ","),
            ]

    def funcMatriculaFICConcomitante(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[3]}" f"{self.index[3]}",
                format(dado["qtdMatriculasFICConcomitante"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[3]}" f"{self.index[3]}",
                format(dado["qtdMatriculasFICConcomitante"]).replace(".", ","),
            ]

    def funcMatriculaFICIntegrado(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[3]}" f"{self.index[4]}",
                format(dado["qtdMatriculasFICIntegrado"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[3]}" f"{self.index[4]}",
                format(dado["qtdMatriculasFICIntegrado"]).replace(".", ","),
            ]

    def funcMatriculaEJAFundamental(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[4]}" f"{self.index[0]}",
                format(dado["qtdMatriculasEJAFundamental"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[4]}" f"{self.index[0]}",
                format(dado["qtdMatriculasEJAFundamental"]).replace(".", ","),
            ]

    def funcMatriculaEJAMedio(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[4]}" f"{self.index[1]}",
                format(dado["qtdMatriculasEJAMedio"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[4]}" f"{self.index[1]}",
                format(dado["qtdMatriculasEJAMedio"]).replace(".", ","),
            ]

    def funcMatriculaEspecialComum(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[5]}" f"{self.index[0]}",
                format(dado["qtdMatriculasEspecialComum"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[5]}" f"{self.index[0]}",
                format(dado["qtdMatriculasEspecialComum"]).replace(".", ","),
            ]

    def funcMatriculaEspecialExclusiva(self, dado, index):
        self.index = index
        if dado["CodigoMunicipio"] == " ":
            return [
                dado["anoSK"] - 2010,
                "00",
                f"{self.index[5]}" f"{self.index[1]}",
                format(dado["qtdMatriculasEspecialExclusiva"]).replace(".", ","),
            ]
        else:
            return [
                dado["anoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[5]}" f"{self.index[1]}",
                format(dado["qtdMatriculasEspecialExclusiva"]).replace(".", ","),
            ]
