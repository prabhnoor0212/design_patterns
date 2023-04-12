from abc import ABC, abstractmethod

class Menu(ABC):
    
    @abstractmethod
    def select_item(self)->None:
        pass