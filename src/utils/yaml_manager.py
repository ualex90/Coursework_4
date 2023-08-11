import yaml

from src.utils.file_manager import FileManager


class YAMLManager(FileManager):

    def load(self):
        pass

    def save(self, data):
        with open(self.file, "w", encoding="UTF-8") as yaml_file:
            yaml.safe_dump(data, yaml_file, sort_keys=False, allow_unicode=True)
