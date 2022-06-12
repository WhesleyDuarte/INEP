import pandas as pd
import numpy as np
import os
import unidecode


sheetName = '1.13'
TipoEnsinoGrupo = "Educaçao Infantil"
NivelTipoEnsino = "Pré-Escola"

NameFileTipoEnsinoGrupo = "EducacaoBasica"

'''
Quando houver necessidade de adicionar o NivelTipoEnsino ao nome do arquivo, adicione o "_" no início.
Ex: _ClassesComuns.
Caso o grupo e o tipo sejma iguais, deixe vazio. Ex: ""
'''
NameFileNivelTipoEnsino = "" 

for year in range(2013,2014):
    fileNameCSV =unidecode.unidecode(f"{year}_fato_tipoDeficiencia_docentes_{NameFileTipoEnsinoGrupo}{NameFileNivelTipoEnsino}.csv".replace(" ", ""))

    pathAbsolute =  os.path.join(os.path.dirname(os.path.abspath(__file__)),f'Sinopse_Estatistica_da_Educacao_Basica_{year}.xlsx')
    
    dataFrame = pd.read_excel(pathAbsolute, sheet_name = sheetName, skiprows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], usecols=[0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14]) 
   
    dataFrame.dropna(axis = 0 , inplace = True) 
    
    dataFrame.rename(columns=
              {
            "Voltar ao Sumário": "Regiao",
            "Unnamed: 1": "Estado",
            "Unnamed: 2": "Municipio",
            "Unnamed: 3": "CodigoMunicipio",
            "Unnamed: 6": "IntegralFederal",
            "Unnamed: 7": "IntegralEstadual",
            "Unnamed: 8": "IntegralMunicipal",
            "Unnamed: 9": "IntegralPrivada",
            "Unnamed: 11": "ParcialFederal",
            "Unnamed: 12": "ParcialEstadual",
            "Unnamed: 13": "ParcialMunicipal",
            "Unnamed: 14": "ParcialPrivada"
        }, inplace = True)

    dataFrame.insert(loc= 0, column = "Ano", value = year, allow_duplicates=False)
    dataFrame.insert(loc= 5, column = "TipoEnsinoGrupo", value = TipoEnsinoGrupo, allow_duplicates=False)
    dataFrame.insert(loc= 6, column = "NivelTipoEnsino", value = NivelTipoEnsino, allow_duplicates=False)
    dataFrame.insert(loc= 1, column = "DEP!", value = "Federal", allow_duplicates=False)
    dataFrame.insert(loc= 2, column = "DEP2", value = "Estadual", allow_duplicates=False)
    dataFrame.insert(loc= 3, column = "DEP3", value = "Municipal", allow_duplicates=False)
    dataFrame.insert(loc= 4, column = "DEP4", value = "Privada", allow_duplicates=False)
'''
    dataFrame.insert(loc= 7, column = "Ano1", value =  "1° Ano", allow_duplicates=False)
    dataFrame.insert(loc= 12, column = "Ano2", value = "2° Ano", allow_duplicates=False)
    dataFrame.insert(loc= 17, column = "Ano3", value = "3° Ano", allow_duplicates=False)
    dataFrame.insert(loc= 22, column = "Ano4", value = "4° Ano", allow_duplicates=False)
    dataFrame.insert(loc= 27, column = "Ano5", value = "5° Ano", allow_duplicates=False)
    dataFrame.insert(loc= 32, column = "DepAdm1", value = "Federal", allow_duplicates=False)
    dataFrame.insert(loc= 33, column = "DepAdm2", value = "Estadual", allow_duplicates=False)
''' 
  

print(dataFrame)
