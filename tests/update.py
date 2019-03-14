#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from config import Config_

class Config(Config_):
    def __init__(self, config_json=''):
        super().__init__(config_json)
        self._set_default('attr1', 1)

config = Config()
config.attr1 = 2
with open('config.pkl', 'wb') as cfile:
    pickle.dump(config, cfile)
with open('config.pkl', 'rb') as cfile:
    new_config = pickle.load(cfile)

config = Config()
config.attr1 = 1
print(config)
print('-' * 80)
config.update(new_config)
print(config)
assert config.attr1 == 2
