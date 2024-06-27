from abc import ABC, abstractmethod


class IResponse(ABC):

    @abstractmethod
    def sucess(self, value: list[dict]) -> dict:
        pass

    @abstractmethod
    def error(self, message: str) -> dict:
        pass
