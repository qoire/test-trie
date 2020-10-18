import abc
from typing import Optional


class Store(abc.ABC):

    @abc.abstractmethod
    def store(self, k: str, v: str) -> None:
        pass

    @abc.abstractmethod
    def load(self, k: str) -> Optional[str]:
        pass