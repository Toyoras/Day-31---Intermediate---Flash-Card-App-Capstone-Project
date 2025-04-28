from app_window import AppWindow
from ui_widgets_builder import UiWidgetsBuilder
from ui_widgets_logic import UiWidgetLogic
from update_csv import UpdateCsv
from config import TIME_BEFORE_CORRECTION

class GameLoop:
    """Brain of the game and link of all classes"""
    def __init__(self, window:AppWindow, widgets_builder:UiWidgetsBuilder, widgets_logic:UiWidgetLogic, update_csv:UpdateCsv) -> None:
       self.window = window 
       self.widgets_builder = widgets_builder
       self.widgets_logic = widgets_logic
       self.update_csv = update_csv
       self.timer_id = None
       self.widgets_logic = widgets_logic

    def init_game(self) -> None:
        self.window.window_init()
        self.widgets_builder.grid_placement()
        self._changing_card()
        self._next_card()

    def _next_card(self) -> None:
        if self.timer_id:
            self.window.window.after_cancel(self.timer_id)
        self.random_row = self.widgets_logic.changing_word()
        self.timer_id = self.window.window.after(TIME_BEFORE_CORRECTION, self.widgets_logic.show_translation)

    def _disable_buttons(self):
        self.widgets_builder.right_button.configure(state="disabled")
        self.widgets_builder.wrong_button.configure(state="disabled")

    def _enable_buttons(self):
        self.widgets_builder.right_button.configure(state="normal")
        self.widgets_builder.wrong_button.configure(state="normal")
    
    def _on_wrong_click(self) -> None:
        self._next_card()

    def _on_right_click(self) -> None:
        self._disable_buttons()
        try:
            self.update_csv.update_word_list(self.widgets_logic.random_row)
            self.widgets_logic.reload_words()
        except Exception as e:
            print(f"Erreur lors de la mise à jour du fichier : {e}")
        finally:
            self._next_card()
            self._enable_buttons()

    def _on_reset_click(self) -> None:
        self.update_csv.reset_csv_files()
        self.widgets_logic.reload_words()
        
    def _changing_card(self) -> None:
        self.widgets_builder.wrong_button.config(command=self._on_wrong_click)
        self.widgets_builder.reset_button.configure(command=self._on_reset_click)
        self.widgets_builder.right_button.config(command=self._on_right_click)