#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
from inherited_config import Config


class Obj:
    def __init__(self):
        self.a = 1 if Config.a == 1 else 2

def test_obj():

    dirname = os.path.dirname(__file__)

    obj = Obj()
    assert obj.a == 1

    Config.load_json(os.path.join(dirname, 'config2.json'))
    obj = Obj()
    assert obj.a == 2


if __name__ == "__main__":
    test_obj()
