from constants import SupportedPlatforms
from ui_android_factory import AndroidUIFactory
from ui_ios_factory import IOSUIFactory

class UIFactoryCreator:
    @classmethod
    def create_factory(cls, ui_type: SupportedPlatforms)->object:
        if ui_type == SupportedPlatforms.ANDROID:
            return AndroidUIFactory()
        elif ui_type == SupportedPlatforms.IOS:
            return IOSUIFactory()
        else:
            raise NotImplementedError(f"{ui_type} is not supported.")