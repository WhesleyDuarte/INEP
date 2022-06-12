class AnosIniciais():
    def __init__(self) -> None:
        pass
    
    def primeiroAnoFederal(self, dado):
        return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano1"],
            dado["DepAdm1"],
            format(dado["primeiroFederal"]).replace(".", ",")   
        ]
        
    def primeiroAnoEstadual(self, dado):
        return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano1"],
            dado["DepAdm2"],
            format(dado["primeiroEstadual"]).replace(".", ",")   
        ]
    
    def primeiroAnoMunicipal(self, dado):
        return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano1"],
            dado["DepAdm3"],
            format(dado["primeiroMunicipal"]).replace(".", ",")   
        ]
    
    def primeiroAnoPrivada(self, dado):
        return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano1"],
            dado["DepAdm4"],
            format(dado["primeiroPrivada"]).replace(".", ",")   
        ]
      
    def segundoAnoFederal(self, dado):
           return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano2"],
            dado["DepAdm1"],
            format(dado["segundoFederal"]).replace(".", ",")   
        ]
           
    def segundoAnoEstadual(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano2"],
        dado["DepAdm2"],
        format(dado["segundoEstadual"]).replace(".", ",")   
    ]
    
    def segundoAnoMunicipal(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano2"],
        dado["DepAdm3"],
        format(dado["segundoMunicipal"]).replace(".", ",")   
    ]
        
    def segundoAnoPrivada(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano2"],
        dado["DepAdm4"],
        format(dado["segundoPrivada"]).replace(".", ",")   
    ]
        
    def terceiroAnoFederal(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano3"],
        dado["DepAdm1"],
        format(dado["terceiroFederal"]).replace(".", ",")   
    ]
        
    def terceiroAnoEstadual(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano3"],
        dado["DepAdm2"],
        format(dado["terceiroEstadual"]).replace(".", ",")   
    ]
    
    def terceiroAnoMunicipal(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano3"],
        dado["DepAdm3"],
        format(dado["terceiroMunicipal"]).replace(".", ",")   
    ]
        
    def terceiroAnoPrivada(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano3"],
        dado["DepAdm4"],
        format(dado["terceiroPrivada"]).replace(".", ",")   
    ]
 
    def quartoAnoFederal(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano4"],
        dado["DepAdm1"],
        format(dado["quartoFederal"]).replace(".", ",")   
    ]
        
    def quartoAnoEstadual(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano4"],
        dado["DepAdm2"],
        format(dado["quartoEstadual"]).replace(".", ",")   
    ]
        
    def quartoAnoMunicipal(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano4"],
        dado["DepAdm3"],
        format(dado["quartoMunicipal"]).replace(".", ",")   
    ]
        
    def quartoAnoPrivada(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano4"],
        dado["DepAdm4"],
        format(dado["quartoPrivada"]).replace(".", ",")   
    ]

    def quintoAnoFederal(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano5"],
        dado["DepAdm1"],
        format(dado["quartoFederal"]).replace(".", ",")   
    ]
    
    def quintoAnoEstadual(self, dado):
        return[
        dado["Ano"],
        dado["CodigoMunicipio"],
        dado["TipoEnsinoGrupo"],
        dado["NivelTipoEnsino"],
        dado["Ano5"],
        dado["DepAdm2"],
        format(dado["quartoEstadual"]).replace(".", ",") 
        ]  
        
    def quintoAnoMunicipal(self, dado):
        return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano5"],
            dado["DepAdm3"],
            format(dado["quartoMunicipal"]).replace(".", ",")
        ]
    def quintoAnoPrivada(self, dado):
        return[
            dado["Ano"],
            dado["CodigoMunicipio"],
            dado["TipoEnsinoGrupo"],
            dado["NivelTipoEnsino"],
            dado["Ano5"],
            dado["DepAdm4"],
            format(dado["quartoPrivada"]).replace(".", ",")
        ]
    
            