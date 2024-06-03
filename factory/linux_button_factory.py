from button_factory import ButtonFactory
from linux_button import LinuxButton


class LinuxButtonFactory(ButtonFactory):
    def create_button(self):
        return LinuxButton()
