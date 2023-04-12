from abc import ABC, abstractmethod
from components.button.button import Button
from components.menu.menu import Menu
from typing import Union
# from ui_android_factory import AndroidUIFactory
# from ui_ios_factory import IOSUIFactory
from constants import SupportedPlatforms


class UIFactory(ABC):

    @abstractmethod
    def create_button(self)->Button:
        pass
    
    @abstractmethod
    def create_menu(self)->Menu:
        pass

    