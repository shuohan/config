# -*- coding: utf-8 -*-

from config import Config


class Obj:
    def __init__(self):
        self.a = 1 if Config.a == 1 else 2
        print(self.a)
