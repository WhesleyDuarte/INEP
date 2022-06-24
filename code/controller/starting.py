from .readerFile import ReaderFile
from .etl import ETL
from .fileGenerator import FileGenerator
from .builderDimension import BuildDimension
from .namenateFile import NamenateFile


class Start(ETL, ReaderFile, FileGenerator, BuildDimension):
    def __init__(self) -> None:
        super().__init__()

    def starting(self, obj, startYear, endYear):
        self.obj = obj
        self.startYear = startYear
        self.endYear = endYear

        for year in range(self.startYear, self.endYear):
            self.nameFileSheet = f"Sinopse_Estatistica_da_Educacao_Basica_{year}.xlsx"

            pathFile = super().searchFile(self.nameFileSheet)

            frame = super().read(
                sheetName=self.obj.sheetName,
                skiprows=self.obj.skiprows,
                usecols=self.obj.usecols,
                nameFileSheet=self.nameFileSheet,
                pathFile=pathFile,
            )

            frame = super().dropna(frame)

            super().renameColumns(frame, self.obj.nameColumns)
            self.obj.newColumns[0].append(year)
            super().insertColumns(
                frame,
                self.obj.newColumns,
            )
            super().generate(obj=self.obj, frame=frame, year=year)
            self.obj.newColumns[0].remove(year)

    def startingDimension(self, obj):
        self.obj = obj

        namingFile = NamenateFile()

        newDimensao = super().buildingDimension(obj=self.obj)
        namingFile.namingFileDimension(sheetName=getattr(obj, "sheetName"), newDimensao=newDimensao)
