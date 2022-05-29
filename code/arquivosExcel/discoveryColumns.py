import pandas as pd
import numpy as np
import os
import unidecode


sheetName = 'Educação Básica 1.1'
TipoEnsinoGrupo = ""
NivelTipoEnsino = ""

NameFileTipoEnsinoGrupo = "EducacaoBasica"

'''
Quando houver necessidade de adicionar o NivelTipoEnsino ao nome do arquivo, adicione o "_" no início.
Ex: _ClassesComuns.
Caso o grupo e o tipo sejma iguais, deixe vazio. Ex: ""
'''
NameFileNivelTipoEnsino = "" 

for year in range(2011,2012):
    fileNameCSV =unidecode.unidecode(f"{year}_fato_tipoDeficiencia_docentes_{NameFileTipoEnsinoGrupo}{NameFileNivelTipoEnsino}.csv".replace(" ", ""))

    pathAbsolute =  os.path.join(os.path.dirname(os.path.abspath(__file__)),f'Sinopse_Estatistica_da_Educacao_Basica_{year}.xlsx')
    
    dataFrame = pd.read_excel(pathAbsolute, sheet_name = sheetName, skiprows = [1,2,3,4,5,6,7,8,9,10,11,12], usecols=[0,1,2,3,6,7,9,10,12,13,14,17,18,19,21,22,24,25,27,28]) 
   
    dataFrame.dropna(axis = 0 , inplace = True) 
     
    dataFrame.rename(columns=
              {'Voltar ao Sumário': 'Regiao', 'Unnamed: 1': 'Estado', 'Unnamed: 2': 'Municipio', 'Unnamed: 3': 'CodigoMunicipio', 'Unnamed: 6': 'qtdMatriculasCreche', 
              'Unnamed: 7': 'qtdMatriculasPreEscola', 'Unnamed: 9': 'qtdMatriculasAnosIniciais','Unnamed: 10' : 'qtdMatriculasAnosFinais', 'Unnamed: 12' : 'qtdMatriculasEnsinoMedioPropedeutico', 
              'Unnamed: 13' : 'qtdMatriculasEnsinoMedioNormal', 'Unnamed: 14' : 'qtdMatriculasEnsinoMedioIntegrado', 'Unnamed: 17' : 'qtdMatriculasProfissionalAssociado',
              'Unnamed: 18' : 'qtdMatriculasProfissionalConcomitante', 'Unnamed: 19' : 'qtdMatriculasProfissionalSubsequente', 'Unnamed: 21' : 'qtdMatriculasFICConcomitante', 
              'Unnamed: 22' : 'qtdMatriculasFICIntegrado', 'Unnamed: 24' : 'qtdMatriculasEJAFundamental', 'Unnamed: 25' : 'qtdMatriculasEJAMedio', 
              'Unnamed: 27' : 'qtdMatriculasEspecialComum', 'Unnamed: 28' : 'qtdMatriculasEspecialExclusiva'}, inplace = True)
''' 
    dataFrame.insert(loc= 0, column = "Ano", value = year, allow_duplicates=False)
    dataFrame.insert(loc= 4, column = "grupoEnsinoSK", value = "Educacao Basica", allow_duplicates=False)

    dataFrame.insert(loc= 0, column = "Ano", value = year, allow_duplicates=False)
    dataFrame.insert(loc= 5, column = "TipoEnsinoGrupo", value = TipoEnsinoGrupo, allow_duplicates=False)
    dataFrame.insert(loc= 6, column = "NivelTipoEnsino", value = NivelTipoEnsino, allow_duplicates=False)
    dataFrame.insert(loc= 7, column = "flag_TipoDeDeficiencia", value = "1", allow_duplicates=False)
    dataFrame.insert(loc= 8, column = "flag_TotalDocentesDeficientes", value = "2", allow_duplicates=False)
    dataFrame.insert(loc= 9, column = "flag_DocentesDeficienciaMultipla", value = "3", allow_duplicates=False)
'''
print(dataFrame)
