from ui_factory import UIFactory
from constants import SupportedPlatforms
from ui_factory_creator import UIFactoryCreator

class Flutter:

    def create_theme(self)->None:
        print("*"*10)
        print("(Flutter) Theme creation is a success! All your life problems will be in Comic Sans from now on.")

    def set_refresh_rate(self)->None:
        print("*"*10)
        print("(Flutter) Refresh rate is set to 75Hz. Let's hope for the best - after all, life's refresh rate is always unpredictable!")

    @classmethod
    def create_UI_factory(cls, ui_type: SupportedPlatforms)->UIFactory:
        return UIFactoryCreator.create_factory(ui_type)
