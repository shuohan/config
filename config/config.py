# -*- coding: utf-8 -*-

import os
import json
from py_singleton import Singleton


class Config_(metaclass=Singleton):
    """Global configurations

    Attributes:
        _loaded (dict): Attributes loaded from the .json file
        _attrs (list): A list of attribute names for printing

    """
    def __init__(self, config_json='configs.json'):
        self._loaded = self._load_json(config_json)
        self._attrs = list()

    def load(self, config_json):
        """Load .json configurations

        Args:
            config_json (str): The filepath to the configuration .json file

        Raises:
            IndexError: .json file has unsupported configurations

        """
        loaded = self._load_json(config_json)
        for key, value in loaded.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise IndexError('Configuration does not have field %s' % key)

    def update(self, config):
        """Update using a Config instance"""
        assert isinstance(config, self.__class__)
        self.__dict__ = config.__dict__

    def save(self, config_json):
        """Save configurations into a .json file

        Args:
            config_json (str): Filepath to the target file

        """
        configs = {key: getattr(self, key) for key in self._attrs}
        with open(config_json, 'w') as jfile:
            json.dump(configs, jfile, indent=4)

    def _set_default(self, key, default):
        """Set the default value if the setting is not in the loaded json file

        Args:
            key (str): The attribute name
            default (anything): The default value of this attribute

        """
        value = self._loaded[key] if key in self._loaded else default
        setattr(self, key, value)
        self._attrs.append(key)

    def _load_json(self, filename):
        """Load json from file

        Args:
            filename (str): The path to the file to load

        """
        loaded = dict()
        if os.path.isfile(filename):
            with open(filename) as json_file:
                loaded = json.load(json_file)
        return loaded

    def __str__(self):
        max_attr_len = max([len(a) for a in self._attrs])
        contents = list()
        contents.append('Configurations')
        for key in self._attrs:
            k = (key+':').ljust(max_attr_len + 1)
            v = str(getattr(self, key))
            contents.append('    %s %s' % (k, v))
        return '\n'.join(contents)
