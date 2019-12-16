#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from inherited_config import Config


class Obj:
    def __init__(self):
        self.a = 1 if Config().a == 1 else 2


def test_obj():

    obj = Obj()
    assert obj.a == 1

    Config().load_json('config2.json')
    obj = Obj()
    assert obj.a == 2
