from flutter import create_theme, set_refresh_rate, create_UI_factory
from constants import SupportedPlatforms

if __name__ == "__main__":
    print("Lesgoooooo! Functional way all the way!")

    create_theme()
    set_refresh_rate()

    create_button, create_menu = create_UI_factory(SupportedPlatforms.ANDROID)
    button_functions = create_button()
    (resize_button, ) = button_functions
    resize_button()
    menu_fucntions = create_menu()
    (select_item, ) = menu_fucntions
    select_item()
