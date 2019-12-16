# -*- coding: utf-8 -*-

import os
import json


class _Singleton(type):
    """Singleton design pattern"""
    _instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class Config(metaclass=_Singleton):
    """Global configurations.

    This class stores the global configurations using the singleton design
    pattern. Inherit this class and define attributes during initialization
    ``__init__``, and use

    >>> Config().attribute = new_value

    to update the attribute. Use

    >>> print(Config())

    to print values of all configurations.

    Note:
        When define the attributes, avoid starting with ``"_"``. Only attributes
        not starting with ``"_"`` are considered configurations.

        When use :class:`Config`, avoid copying the attribute values since the new
        variables do not update their values automatically when :class:`Config`
        attributes changes.

    """
    def load_json(self, filepath):
        """Loads configurations from a ``".json"`` file.

        Note:
            Any field in the ``".json"`` file should be a class attribute of
            this class.

        Args:
            filepath (str): The filepath to the configuration file.

        Raises:
            KeyError: A field is not in the class attributes.

        """
        with open(filepath) as jfile:
            loaded = json.load(jfile)
        self.load_dict(loaded)

    def load_dict(self, config):
        """Loads configurations from a :class:`dict`.

        Note:
            Any field in the :class:`dict` should be a class attribute of this
            class.

        Args:
            config (dict): The configurations to load.

        Raises:
            KeyError: A field is not in the class attributes.

        """
        attrs = self._get_attrs()
        for key, value in config.items():
            if key in attrs:
                setattr(self, key, value)
            else:
                raise KeyError('Config does not have the field %s' % key)

    def save_json(self, filepath):
        """Saves configurations into a ``".json"`` file.

        Args:
            filepath (str): The filepath to the target file.

        """
        with open(filepath, 'w') as jfile:
            json.dump(self.save_dict(), jfile, indent=4)

    def save_dict(self):
        """Saves configurations into a a :class:`dict`."""
        return {key: getattr(self, key) for key in self._get_attrs()}

    def _get_attrs(self):
        """Returns all configuration attributes."""
        return [attr for attr in dir(self)
                if not callable(getattr(self, attr))
                and not attr.startswith('_')]

    def __str__(self):
        """Prints out all configurations."""
        attrs = self._get_attrs()
        max_attr_len = max([len(a) for a in attrs])
        message = list()
        message.append('Configurations')
        pattern = '    %%%ds: %%s' % max_attr_len
        for key in attrs:
            value = str(getattr(self, key))
            message.append(pattern % (key, value))
        return '\n'.join(message)
