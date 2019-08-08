# -*- coding: utf-8 -*-

import os
import json


class Config:
    """Global configurations.

    Store the global configurations as class attributes. Use

    >>> Config.attribute = new_value

    instead of initializing an instance to update the attribute. This class
    supports loading configurations from a ``".json"`` file and saving. Call the
    method :meth:`show` to print out values of all configurations.

    """
    def __init__(self):
        raise RuntimeError('The class "Config" should not be initialized')

    @classmethod
    def _get_attrs(cls):
        """Returns all attributes."""
        return [attr for attr in dir(cls)
                if not callable(getattr(cls, attr))
                and not attr.startswith('__')]

    @classmethod
    def show(cls):
        """Prints out all configurations."""
        attrs = cls._get_attrs()
        max_attr_len = max([len(a) for a in attrs])
        message = list()
        message.append('Configurations')
        pattern = '    %%%ds: %%s' % max_attr_len
        for key in attrs:
            value = str(getattr(cls, key))
            message.append(pattern % (key, value))
        print('\n'.join(message))

    @classmethod
    def load_json(cls, filepath):
        """Loads configurations from a ``".json"`` file.

        Note:
            Any field in the ``".json"`` file should be a class attribute of
            this class.

        Args:
            filepath (str): The filepath to the configuration file.

        """
        with open(filepath) as jfile:
            loaded = json.load(jfile)
        cls.load_dict(loaded)

    @classmethod
    def load_dict(cls, config):
        """Loads configurations from a :class:`dict`.

        Note:
            Any field in the :class:`dict` should be a class attribute of this
            class.

        Args:
            config (dict): The configurations to load.

        Raises:
            KeyError: A field is not in the class attributes.

        """
        for key, value in config.items():
            if hasattr(cls, key):
                setattr(cls, key, value)
            else:
                raise KeyError('Config does not have the field %s' % key)

    @classmethod
    def save_json(cls, filepath):
        """Saves configurations into a ``".json"`` file.

        Args:
            filepath (str): The filepath to the target file.

        """
        with open(filepath, 'w') as jfile:
            json.dump(cls.save_dict(), jfile, indent=4)

    @classmethod
    def save_dict(cls):
        """Returns a :class:`dict` of all configurations."""
        return {key: getattr(cls, key) for key in cls._get_attrs()}
