from app_window import AppWindow
from language_setting import LanguageSettings
import tkinter as tk
import customtkinter as ctk
from config import (
    IMAGE_BG_BACK, 
    IMAGE_BG_FRONT, 
    IMAGE_RIGHT, 
    IMAGE_WRONG, 
    CANVAS_SIZE_HEIGHT, 
    CANVAS_SIZE_WIDTH, 
    BACKGROUND_COLOR, 
    IMAGE_BG_LOCATION_X, 
    IMAGE_BG_LOCATION_Y, 
    LANGUAGE_Y, WORD_Y, 
    FONT_NAME, 
    FONT_LANGUAGE_SIZE, 
    FONT_LANGUAGE_STYLE, 
    FONT_WORD_SIZE, 
    FONT_WORD_STYLE,
    BUTTON_FG_COLOR, 
    BUTTON_TEXT_COLOR, 
    BUTTON_FONT_NAME, 
    BUTTON_FONT_SIZE,
    BUTTON_FONT_STYLE, 
    BUTTON_HOVER_COLOR
    )

class UiWidgetsBuilder: 
    """Build all GUI Items"""
    def __init__(self, parent:AppWindow, language_settings: LanguageSettings) -> None:
        self.parent = parent.window
        self.language_settings = language_settings
        # Images loading
        self.front_language_image = tk.PhotoImage(file=IMAGE_BG_FRONT)
        self.back_language_image = tk.PhotoImage(file=IMAGE_BG_BACK)
        self.wrong = tk.PhotoImage(file=IMAGE_WRONG)
        self.right = tk.PhotoImage(file=IMAGE_RIGHT)
        # Card initial config
        self.canvas = tk.Canvas(self.parent, width=CANVAS_SIZE_WIDTH, height=CANVAS_SIZE_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.bg_image = self.canvas.create_image(IMAGE_BG_LOCATION_X, IMAGE_BG_LOCATION_Y, image=self.front_language_image)
        self.language_text = self.canvas.create_text(IMAGE_BG_LOCATION_X, LANGUAGE_Y, text=self.language_settings.learned_language, font=(FONT_NAME, FONT_LANGUAGE_SIZE, FONT_LANGUAGE_STYLE))
        self.word_text = self.canvas.create_text(IMAGE_BG_LOCATION_X, WORD_Y, font=(FONT_NAME, FONT_WORD_SIZE, FONT_WORD_STYLE))
        # Buttons
        self.wrong_button = tk.Button(self.parent, image=self.wrong, highlightthickness=0, borderwidth=0, relief="flat")
        self.reset_button = ctk.CTkButton(
            self.parent, 
            text="Reset Data", 
            bg_color=BACKGROUND_COLOR, 
            fg_color=BUTTON_FG_COLOR, 
            text_color=BUTTON_TEXT_COLOR, 
            font=(BUTTON_FONT_NAME, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE), 
            hover_color=BUTTON_HOVER_COLOR, 
            corner_radius=15) 
        self.right_button = tk.Button(self.parent, image=self.right, highlightthickness=0, borderwidth=0, relief="flat")
        
    def grid_placement(self) -> None:
        self.canvas.grid(column=0, row=0, columnspan=3)
        self.wrong_button.grid(column=0, row=1)
        self.reset_button.grid(column=1, row=1)
        self.right_button.grid(column=2, row=1)