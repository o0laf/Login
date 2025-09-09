from abc import ABC, abstractmethod

class IAuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, identifier, password):
        pass