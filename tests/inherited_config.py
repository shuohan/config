#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from config import Config as _Config


class Config(_Config):
    """Global configurations.

    """
    def __init__(self):
        self.a = 1
        self.b = 2


def test_config():
    dirname = os.path.dirname(__file__)
    config1 = os.path.join(dirname, 'config1.json')
    config2 = os.path.join(dirname, 'config2.json')

    print(Config())
    assert Config().a == 1
    Config().save_json(config1)
    with open(config1) as jfile:
        assert json.load(jfile) == dict(a=1, b=2)
    Config().load_json(config2)
    print(Config())
    assert Config().a == 11
    Config().a = 100
    assert Config().a == 100
    print(Config())
    try:
        Config().load_dict(dict(c=9))
    except KeyError: 
        assert True


if __name__ == "__main__":
    test_config()
