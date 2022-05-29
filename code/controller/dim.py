import pandas as pd
import numpy as np
import unidecode


etapaEnsino = [
    "Educação Infantil",
    "Ensino Fundamental",
    "Ensino Médio",
    "Educação Profissional",
    "Educação de Jovens e Adultos - EJA",
    "Educação Especial",
]
etapaEnsinoSK = ["1", "2", "3", "4", "5", "6"]
nivelEnsino = [
    "Creche",
    "Pré-Escola",
    "Anos Iniciais",
    "Anos Finais",
    "Ensino Médio Propedêutico",
    "Ensino Médio Normal/Magistério",
    "Curso Técnico Integrado (Ensino Médio Integrado)",
    "Associada ao Ensino Médio",
    "Curso Técnico Concomitante",
    "Curso Técnico Subsequente",
    "Curso FIC Concomitante",
    "Curso FIC Integrado na Modalidade EJA",
    "Ensino Fundamental",
    "Ensino Médio",
    "Classes Comuns",
    "Classes Exclusivas",
]
nivelEnsinoSK = ["1", "2", "3", "4", "5"]

# Criação de dataframe com as combinações das listas
dataFrame = pd.DataFrame(
    data={
        "grupoensinoSK": [
            etapaEnsinoSK[0] + nivelEnsinoSK[0],
            etapaEnsinoSK[0] + nivelEnsinoSK[1],
            etapaEnsinoSK[1] + nivelEnsinoSK[0],
            etapaEnsinoSK[1] + nivelEnsinoSK[1],
            etapaEnsinoSK[2] + nivelEnsinoSK[0],
            etapaEnsinoSK[2] + nivelEnsinoSK[1],
            etapaEnsinoSK[2] + nivelEnsinoSK[2],
            etapaEnsinoSK[3] + nivelEnsinoSK[0],
            etapaEnsinoSK[3] + nivelEnsinoSK[1],
            etapaEnsinoSK[3] + nivelEnsinoSK[2],
            etapaEnsinoSK[3] + nivelEnsinoSK[3],
            etapaEnsinoSK[3] + nivelEnsinoSK[4],
            etapaEnsinoSK[4] + nivelEnsinoSK[0],
            etapaEnsinoSK[4] + nivelEnsinoSK[1],
            etapaEnsinoSK[5] + nivelEnsinoSK[0],
            etapaEnsinoSK[5] + nivelEnsinoSK[1],
        ],
        "etapaEnsino": [
            etapaEnsino[0],
            etapaEnsino[0],
            etapaEnsino[1],
            etapaEnsino[1],
            etapaEnsino[2],
            etapaEnsino[2],
            etapaEnsino[2],
            etapaEnsino[3],
            etapaEnsino[3],
            etapaEnsino[3],
            etapaEnsino[3],
            etapaEnsino[3],
            etapaEnsino[4],
            etapaEnsino[4],
            etapaEnsino[5],
            etapaEnsino[5],
        ],
        "nivelEnsino": [
            nivelEnsino[0],
            nivelEnsino[1],
            nivelEnsino[2],
            nivelEnsino[3],
            nivelEnsino[4],
            nivelEnsino[5],
            nivelEnsino[6],
            nivelEnsino[7],
            nivelEnsino[8],
            nivelEnsino[9],
            nivelEnsino[10],
            nivelEnsino[11],
            nivelEnsino[12],
            nivelEnsino[13],
            nivelEnsino[14],
            nivelEnsino[15],
        ],
    }
)

# Gerar o arquivo CSV
fileNameCSV = unidecode.unidecode("dim_grupoEnsino.csv".replace(" ", ""))
np.savetxt(
    fileNameCSV,
    dataFrame,
    delimiter=";",
    fmt="%s",
    encoding="utf-8",
    header="grupoEnsinoSK;etapaEnsino;nivelEnsino",
    comments="",
)
print(f"Arquivo: {fileNameCSV} gerado com Sucesso!!!")