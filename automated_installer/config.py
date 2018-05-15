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


    def save(self, path):
        pass
