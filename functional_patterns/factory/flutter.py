from constants import SupportedPlatforms
from typing import Callable, Tuple
from ui_factory_creator import create_factory

def create_theme()->None:
    print("*"*10)
    print("(Flutter) Theme creation is a success! All your life problems will be in Comic Sans from now on.")

def set_refresh_rate()->None:
    print("*"*10)
    print("(Flutter) Refresh rate is set to 75Hz. Let's hope for the best - after all, life's refresh rate is always unpredictable!")

def create_UI_factory(ui_type: SupportedPlatforms) -> Tuple[Callable, Callable]:
    return create_factory(ui_type)