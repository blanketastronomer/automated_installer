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
        """
        Class constructor.  Takes a variable number of arguments.

        Args:
            **main_directory (str): The top-level directory where the utility will execute.
            **installer_root (str): The directory where all installers are kept.
            **application_root (str): The directory where all system applications should be installed.
            **application_32_root (str): (Windows only) The directory where all 32-bit applications should be installed.
        """

        if os.name == 'nt':
            self.config_object.home_directory = os.path.expandvars('$USERPROFILE')
        else:
            self.config_object.home_directory = os.path.expandvars('$HOME')

        arguments = ['main_directory', 'installer_root', 'application_root', 'application_32_root', 'installers']

        for arg in arguments:
            if arg == 'installers':
                self.config_object[arg] = kwargs.get(arg, [])
            else:
                self.config_object[arg] = kwargs.get(arg, '')

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
