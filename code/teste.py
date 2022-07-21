x={"NewColumns": [
    [0, "Ano"],
    [1, "DepAdm1", "Federal"],
    [2, "DepAdm2", "Estadual"],
    [3, "DepAdm3", "Municipal"],
    [4, "DepAdm4", "Privada"],
    [4, "TipoEnsinoGrupo", "Educaçao Infantil"],
    [5, "NivelTipoEnsino", "Creche"],
    [6, "LocalizacaoUrb", "Urbana"],
    [12, "LocalizacaoRural", "Rural"]
]
}
print(type(x))

#for indx in x["NewColumns"]:
 #   print(indx[])
x["NewColumns"][0].append(2013)
print(x["NewColumns"][0])