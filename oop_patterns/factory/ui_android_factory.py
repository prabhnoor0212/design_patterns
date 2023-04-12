from ui_factory import UIFactory
from components.button.android_button import AndroidButton
from components.menu.android_menu import AndroidMenu

class AndroidUIFactory(UIFactory):
    def create_button(self)->AndroidButton:
        print("*"*10)
        print("(Android) Button is created! Press it to remind yourself of all the life problems you've been avoiding and kickstart a full-blown existential crisis!")
        print("Just kidding!")
        print("But why are you creating android objects on apple device?")
        button = AndroidButton()
        return button
    
    def create_menu(self)->AndroidMenu:
        print("*"*10)
        print("(Android) Menu is created, making decisions harder than they need to be")
        menu = AndroidMenu()
        return menu