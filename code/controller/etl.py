import pandas as pd


class ETL:
    def __init__(self) -> None:
        pass

    def dropna(self, frame):

        self.frame = frame
        return pd.DataFrame.dropna(self.frame)

    def renameColumns(self, frame, nameColumns):

        self.frame = pd.DataFrame(frame)
        self.nameColumns = nameColumns
        return self.frame.rename(columns=self.nameColumns, inplace=True)

    def insertColumns(self, frame, newColumns):

        self.newColumns = newColumns
        self.frame = pd.DataFrame(frame)

        for item in self.newColumns:

            self.frame.insert(
                loc=item[0], column=item[1], value=item[2], allow_duplicates=False
            )
