from .abaModel import AbaModel


class Dimension(AbaModel):
    def __init__(self, sheetName, dimensao, header):
        super().__init__(sheetName=sheetName, header=header)
        self.dimensao = dimensao
