from abc import ABC, abstractmethod

class AbstractPage(ABC):
    
    @abstractmethod
    def get_module_name(self):
        pass

    @abstractmethod
    def get_class_name(self):
        pass

    @abstractmethod
    def write_class_file(self):
        pass