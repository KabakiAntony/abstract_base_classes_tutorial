from abc import ABCMeta, abstractmethod


class MyAbstractClass(metaclass=ABCMeta):
    
    @abstractmethod
    def my_abstract_method(self):
        pass
