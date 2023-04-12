from flutter import Flutter
from constants import SupportedPlatforms

if __name__ == "__main__":
    print("Lesgoooooo!")

    f_obj = Flutter()
    f_obj.create_theme()
    f_obj.set_refresh_rate()

    ui_fac = Flutter.create_UI_factory(SupportedPlatforms.ANDROID)
    button = ui_fac.create_button()
    button.resize_button()
    menu = ui_fac.create_menu()
    menu.select_item()
