from model.abaModel import AbaModel

class AbaNota(AbaModel):
    def __init__(self) -> None:
        super().__init__()
        self.index = self.obj["Index"]