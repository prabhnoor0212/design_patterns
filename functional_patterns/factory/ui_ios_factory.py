from components.button.ios_button import resize_button
from components.menu.ios_menu import select_item
from typing import Callable, Tuple

def create_button()->Tuple[Callable]:
    print("*"*10)
    print("(IOS) Button is created! Press it to remind yourself of all the life problems you've been avoiding and kickstart a full-blown existential crisis!")
    print("Just kidding!")
    return (resize_button, )

def create_menu()->Tuple[Callable]:
    print("*"*10)
    print("(IOS) Menu is created, making decisions harder than they need to be")
    return (select_item, )