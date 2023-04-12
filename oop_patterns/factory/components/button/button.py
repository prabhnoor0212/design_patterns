from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def resize_button(self)->None:
        pass