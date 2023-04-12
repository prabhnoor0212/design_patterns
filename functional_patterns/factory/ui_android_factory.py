from components.button.android_button import resize_button
from components.menu.android_menu import select_item
from typing import Callable, Tuple

def create_button()->Tuple[Callable]:
    print("*"*10)
    print("(Android) Button is created! Press it to remind yourself of all the life problems you've been avoiding and kickstart a full-blown existential crisis!")
    print("Just kidding!")
    print("But why are you creating android objects on apple device?")
    return (resize_button,)

def create_menu()->Tuple[Callable]:
    print("*"*10)
    print("(Android) Menu is created, making decisions harder than they need to be")
    return (select_item,)