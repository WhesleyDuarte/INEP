from asyncio.windows_events import NULL
from tracemalloc import start

from black import nullcontext
from controller.etl import ETL
from controller.readerFile import ReaderFile
from controller.fileGenerator import FileGenerator
from controller.starting import Start


class Main(Start):
    def __init__(self) -> None:
        pass

    def start(self, obj, startYear, endYear):
        self.startYear = startYear
        self.endYear = endYear
        self.obj = obj
        super().starting(obj=self.obj, startYear=self.startYear, endYear=self.endYear)
