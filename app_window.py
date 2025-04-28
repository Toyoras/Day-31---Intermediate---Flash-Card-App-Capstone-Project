import customtkinter as ctk
from config import (
    WINDOW_PADX, 
    WINDOW_PADY, 
    BACKGROUND_COLOR
    )

class AppWindow:
    """Window settings"""
    def __init__(self) -> None:
        self.window = ctk.CTk()

    def window_init(self) -> None:
        self.window.title("Flashy")
        self.window.config(padx=WINDOW_PADX, pady=WINDOW_PADY, bg=BACKGROUND_COLOR)
    
    def stay_open(self) -> None:
        self.window.mainloop()
