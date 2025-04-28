from language_setting import LanguageSettings
import pandas
import os
from config import (
    WORDS_DATA_FILE,
    LEARNED_WORDS_DATA_FILE
    )

class UpdateCsv:
    """Update in CSV Files"""
    def __init__(self, language_settings: LanguageSettings) -> None:
        self.word_df = pandas.read_csv(WORDS_DATA_FILE)
        self.learned_words_df = None
        self.language_settings = language_settings
    
    def update_word_list(self, random_row) -> None:
        self.learned_words_df = pandas.DataFrame(random_row)
        self.word_df = self.word_df.drop(index=random_row.index)
        self.word_df = self.word_df.reset_index(drop=True)
        learned_words_df_exists = os.path.exists(LEARNED_WORDS_DATA_FILE)
        self.learned_words_df.to_csv(LEARNED_WORDS_DATA_FILE, mode="a", header=not learned_words_df_exists, index=False)
        self.word_df.to_csv(WORDS_DATA_FILE, index=False)
    
    def reset_csv_files(self) -> None:
        if os.path.exists(LEARNED_WORDS_DATA_FILE):
            self.learned_words_df = pandas.read_csv(LEARNED_WORDS_DATA_FILE)
        else:
            self.learned_words_df = pandas.DataFrame(columns=[self.language_settings.learned_language, self.language_settings.native_language])

        reseted_file = pandas.concat([self.word_df, self.learned_words_df], ignore_index=True)
        reseted_file.to_csv(WORDS_DATA_FILE, index=False)

        empty_learned_file = pandas.DataFrame(columns=[self.language_settings.learned_language, self.language_settings.native_language])
        empty_learned_file.to_csv(LEARNED_WORDS_DATA_FILE, index=False)

        self.word_df = pandas.read_csv(WORDS_DATA_FILE)