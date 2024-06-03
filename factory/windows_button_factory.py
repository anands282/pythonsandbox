from button_factory import ButtonFactory
from windows_button import WindowsButton


class WindowsButtonFactory(ButtonFactory):
    def create_button(self):
        return WindowsButton()
