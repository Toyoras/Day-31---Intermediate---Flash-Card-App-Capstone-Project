from ui_widgets_builder import UiWidgetsBuilder
from typing import Callable
from language_setting import LanguageSettings
import pandas 
from CTkMessagebox import CTkMessagebox
from config import(
    WORDS_DATA_FILE,
    BACKGROUND_COLOR, 
    BUTTON_FG_COLOR, 
    BUTTON_MESSAGEBOX_FG_COLOR, 
    BUTTON_HOVER_COLOR, 
    BUTTON_TEXT_COLOR 
    )


class UiWidgetLogic:
    """Logic for GUI Items"""
    def __init__(self, builder:UiWidgetsBuilder, reset_files_callback:Callable, language_settings: LanguageSettings) -> None:
        self.builder = builder
        self.words_df = pandas.read_csv(WORDS_DATA_FILE)
        self.random_row = None
        self.reset_files_callback = reset_files_callback
        self.language_settings = language_settings

    def changing_word(self) -> object:
        if self.words_df.empty:
            response = CTkMessagebox(
                title=" ",
                message="Congratulations !\nYou've learned all the words !\nDo you want to play again ?",
                icon="question",
                option_1="Yes",
                option_2="No",
                bg_color=BACKGROUND_COLOR,           
                fg_color=BUTTON_MESSAGEBOX_FG_COLOR,              
                button_color=BUTTON_FG_COLOR,          
                button_hover_color=BUTTON_HOVER_COLOR,
                text_color=BUTTON_TEXT_COLOR
            ).get()
            if response == "Yes":
                self.reset_files_callback()
            return None
        else:
            self.random_row = self.words_df.sample(n=1)
            word = self.random_row[self.language_settings.learned_language].values[0]
            self.builder.canvas.itemconfig(self.builder.word_text, text=word)
            self.builder.canvas.itemconfig(self.builder.bg_image, image=self.builder.front_language_image)
            self.builder.canvas.itemconfig(self.builder.language_text, text=self.language_settings.learned_language)
            return self.random_row

    def show_translation(self) -> None:
        word_translated = self.random_row[self.language_settings.native_language].values[0]
        self.builder.canvas.itemconfig(self.builder.bg_image, image=self.builder.back_language_image)
        self.builder.canvas.itemconfig(self.builder.language_text, text=self.language_settings.native_language)
        self.builder.canvas.itemconfig(self.builder.word_text, text=word_translated)

    def reload_words(self) -> None:
        self.words_df = pandas.read_csv(WORDS_DATA_FILE)
