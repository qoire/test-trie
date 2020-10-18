import abc
import json
from typing import Union, Any, List


class Codec(abc.ABC):

    @abc.abstractmethod
    def serialize(self, node: List[str]) -> str:
        pass

    @abc.abstractmethod
    def deserialize(self, s: str) -> List[str]:
        pass


class JsonCodec(Codec):
    def __init__(self):
        pass

    @abc.abstractmethod
    def serialize(self, node: List[Union[str, None]]) -> str:
        # sanity check
        for n in node:
            if not (n is None or isinstance(n, str)):
                raise TypeError("invalid type")
        return json.dumps(node)

    @abc.abstractmethod
    def deserialize(self, s: str) -> List[str]:
        return json.loads(s)