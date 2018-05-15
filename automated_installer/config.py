import os
import json
from dotmap import DotMap


class Config(object):
    """
    Handles everything related to configuration.

    This includes saving and loading configuration files.
    """
    config_object = DotMap()

    def __init__(self, **kwargs):
        pass

    def load(self, path):
        pass

    def save(self, path: str) -> None:
        """
        Saves the current configuration to a file.

        Args:
            path (str): Path to the save file.
        """
        try:
            with open(path, 'w') as write_file:
                json.dump(self.config_object, write_file, indent=True)
        except FileNotFoundError:
            print(f"The system cannot find the specified config file at {os.path.abspath(path)}")
