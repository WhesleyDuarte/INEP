from abaModel import AbaModel


class AbaNota(AbaModel):
    def __init__(self, sheetName, index) -> None:
        super().__init__(sheetName)
        self.index = index
