#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import Config as _Config


class Config(_Config):
    """Global configurations.

    """
    a = 1
    """int: The first attribute."""
    attr = 2
    """int: The second attribute."""


if __name__ == "__main__":
    Config.show()
    Config.save_json('config1.json')
    Config.load_json('config2.json')
    Config.show()
    Config.a = 100
    Config.show()
