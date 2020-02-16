from abc import ABC, abstractmethod
from pathlib import Path


class BaseDownloader(ABC):
    def __init__(self, link: str, path: Path):
        self.link = link
        self.path = path

    @abstractmethod
    def start(self) -> None:
        pass

