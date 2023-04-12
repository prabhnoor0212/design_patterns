from constants import SupportedPlatforms
from typing import Callable, Tuple
from ui_android_factory import (
    create_button as create_button_android, 
    create_menu as create_menu_android
    )
from ui_ios_factory import (
    create_button as create_button_ios, 
    create_menu as create_menu_ios
    )




def create_factory(ui_type: SupportedPlatforms)->Tuple[Callable, Callable]:
    if ui_type == SupportedPlatforms.ANDROID:
        create_button = create_button_android
        create_menu = create_menu_android
    elif ui_type == SupportedPlatforms.IOS:
        create_button = create_button_ios
        create_menu = create_menu_ios
    else:
        raise NotImplementedError(f"{ui_type} is not supported.")
    return (create_button, create_menu)