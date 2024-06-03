from button_factory import ButtonFactory
from windows_button_factory import WindowsButtonFactory
from linux_button_factory import LinuxButtonFactory


class Render:
    def render_button(factory: ButtonFactory):
        button = factory.create_button()
        print(button.render())

    if __name__ == "__main__":
        windows_factory = WindowsButtonFactory()
        linux_factory = LinuxButtonFactory()

        render_button(windows_factory)
        render_button(linux_factory)

