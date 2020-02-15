from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class LiveInfo:
    uname: str
    title: str
    suffix: str


class BaseParse(ABC):
    def __str__(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def link(self) -> str:
        pass

    @abstractmethod
    async def info(self) -> LiveInfo:
        pass
