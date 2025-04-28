class LanguageSettings:
    """Set the language learned and native for all classes"""
    def __init__(self, learned_language: str, native_language: str)-> None:
        self.learned_language = learned_language
        self.native_language = native_language