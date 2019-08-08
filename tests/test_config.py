#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from inherited_config import Config


class Obj:
    def __init__(self):
        self.a = 1 if Config.a == 1 else 2
        print(self.a)


Config.show()
Config.save_json('config1.json')
obj = Obj()

Config.load_json('config2.json')
Config.show()

Config.b = 100
Config.show()
obj = Obj()
