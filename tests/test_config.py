#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from config import Config
from obj import Obj

Config.a = 1
Config.attr = 2
Config.show()
Config.save_json('config1.json')
obj = Obj()

Config.load_json('config2.json')
Config.show()

Config.b = 100
Config.show()
obj = Obj()
