import pandas
from config import WORDS_DATA_FILE

class LanguageExtractor:
    def __init__(self) -> None:
        self.csv_path = WORDS_DATA_FILE

    def extract(self) -> tuple[str, str]:
        df = pandas.read_csv(self.csv_path)
        columns = df.columns.tolist()
        if len(columns) < 2:
            raise ValueError("CSV must have at least two columns")
        return columns[0], columns[1]