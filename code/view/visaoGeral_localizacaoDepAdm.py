

class VisaoGeralLocalizacaoDepAdministrativa():
    def __init__(self) -> None:
        pass

    def funcMatriculaTotalLocalizacaoDepAdministrativa(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                "00",
                "00",
                format(dado["TotalMatriculas"]).replace(".", ","),
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                "00",
                "00",
                format(dado["TotalMatriculas"]).replace(".", ","),
            ]
    
    def funcMatriculaUrbanaFederal(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[0]}",
                f"{self.index[0]}",
                format(dado["MatriculasUrbanaFederal"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[0]}",
                f"{self.index[0]}",
                format(dado["MatriculasUrbanaFederal"]).replace(".", ",")
            ]

    def funcMatriculaUrbanaEstadual(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[0]}",
                f"{self.index[1]}",
                format(dado["MatriculasUrbanaEstadual"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[0]}",
                f"{self.index[1]}",
                format(dado["MatriculasUrbanaEstadual"]).replace(".", ",")
            ]

    def funcMatriculaUrbanaMunicipal(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[0]}",
                f"{self.index[2]}",
                format(dado["MatriculasUrbanaMunicipal"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[0]}",
                f"{self.index[2]}",
                format(dado["MatriculasUrbanaMunicipal"]).replace(".", ",")
            ]

    def funcMatriculaUrbanaPrivada(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[0]}",
                f"{self.index[3]}",
                format(dado["MatriculasUrbanaPrivada"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[0]}",
                f"{self.index[3]}",
                format(dado["MatriculasUrbanaPrivada"]).replace(".", ",")
            ]

    def funcMatriculaRuralFederal(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[1]}",
                f"{self.index[0]}",
                format(dado["MatriculasRuralFederal"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[1]}",
                f"{self.index[0]}",
                format(dado["MatriculasRuralFederal"]).replace(".", ",")
            ]

    def funcMatriculaRuralEstadual(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[1]}",
                f"{self.index[1]}",
                format(dado["MatriculasRuralEstadual"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[1]}",
                f"{self.index[1]}",
                format(dado["MatriculasRuralEstadual"]).replace(".", ",")
            ]

    def funcMatriculaRuralMunicipal(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[1]}",
                f"{self.index[2]}",
                format(dado["MatriculasRuralMunicipal"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[1]}",
                f"{self.index[2]}",
                format(dado["MatriculasRuralMunicipal"]).replace(".", ",")
            ]

    def funcMatriculaRuralPrivada(self, dado, index):
        self.index = index

        if dado["CodigoMunicipio"] == " ":
            return [
                dado["AnoSK"] - 2010,
                "00",
                f"{self.index[1]}",
                f"{self.index[3]}",
                format(dado["MatriculasRuralPrivada"]).replace(".", ",")
            ]
        else:
            return [
                dado["AnoSK"] - 2010,
                dado["CodigoMunicipio"],
                f"{self.index[1]}",
                f"{self.index[3]}",
                format(dado["MatriculasRuralPrivada"]).replace(".", ",")
            ]