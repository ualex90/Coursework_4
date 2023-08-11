from abc import ABC, abstractmethod
from pathlib import Path

from settings import FIXTURES


class FileManager(ABC):
    def __init__(self, file_name):
        self.file = Path(FIXTURES, file_name)

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, data):
        pass
