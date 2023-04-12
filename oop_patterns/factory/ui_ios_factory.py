from ui_factory import UIFactory
from components.button.ios_button import IOSButton
from components.menu.ios_menu import IOSMenu

class IOSUIFactory(UIFactory):
    def create_button(self)->None:
        print("*"*10)
        print("(IOS) Button is created! Press it to remind yourself of all the life problems you've been avoiding and kickstart a full-blown existential crisis!")
        print("Just kidding!")
        button = IOSButton()
        return button
    
    def create_menu(self)->None:
        print("*"*10)
        print("(IOS) Menu is created, making decisions harder than they need to be")
        menu = IOSMenu()
        return menu