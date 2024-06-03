from abc import ABC, abstractmethod


class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
