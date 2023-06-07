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
        else:
            self._language = "EN"
        return self


class Keyboard(LanguageMixin, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)






# class LanguageMixin:
#     def __init__(self):
#         self._language = "EN"
#
#     @property
#     def language(self):
#         return self._language
#
#     @language.setter
#     def language(self, value):
#         if value not in ["EN", "RU"]:
#             raise ValueError("Invalid language. Supported languages: EN, RU")
#         self._language = value
#
#     def change_lang(self):
#         if self._language == "EN":
#             self._language = "RU"
#         else:
#             self._language = "EN"
#         return self
#
#
# class Keyboard(Item, LanguageMixin):
#     def __init__(self, name, price, quantity):
#         super().__init__(name, price, quantity)
#
#     def __repr__(self):
#         return f"Keyboard('{self.name}', {self.price}, {self.quantity})"
#
#     def __str__(self):
#         return self.name





