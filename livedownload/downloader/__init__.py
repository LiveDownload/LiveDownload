from abc import ABC, abstractmethod


class BaseDownloader(ABC):
    def __init__(self, link: str, name: str):
        self.link = link
        self.name = name

    @abstractmethod
    def start(self) -> None:
        pass

