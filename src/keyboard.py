from src.item import Item


class LanguageMixin:
    _language = "EN"

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
            return self
        else:
            self._language = "EN"
            return self


class Keyboard(LanguageMixin, Item):
    @property
    def language(self):
        return self._language

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)








