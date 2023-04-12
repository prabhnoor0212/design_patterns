from components.menu.menu import Menu

class IOSMenu(Menu):
    def select_item(self) -> None:
        print("*"*10)
        print("(IOS) Ah! You selected to do nothing. A person of cuture?")