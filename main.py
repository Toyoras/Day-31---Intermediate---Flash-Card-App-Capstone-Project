from app_window import AppWindow
from language_setting import LanguageSettings
from ui_widgets_builder import UiWidgetsBuilder
from ui_widgets_logic import UiWidgetLogic
from update_csv import UpdateCsv
from game_loop import GameLoop
from language_extractor import LanguageExtractor

def main() -> None:
    window = AppWindow()
    extractor = LanguageExtractor()
    learned_language, native_language = extractor.extract()
    language_settings = LanguageSettings(learned_language, native_language)
    widgets_builder = UiWidgetsBuilder(window,language_settings)
    update_csv = UpdateCsv(language_settings)
    widgets_logic = UiWidgetLogic(widgets_builder, update_csv.reset_csv_files, language_settings)

    game_loop = GameLoop(window, widgets_builder, widgets_logic, update_csv)

    game_loop.init_game()

    window.stay_open()

# ----- LAUNCH -----
if __name__ == "__main__":
    main()