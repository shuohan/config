#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import Config as _Config


class Config(_Config):
    """Global configurations.

    """
    def __init__(self):
        self.a = 1
        self.b = 2


if __name__ == "__main__":
    print(Config())
    Config().save_json('config1.json')
    Config().load_json('config2.json')
    print(Config())
    Config().a = 100
    print(Config())
