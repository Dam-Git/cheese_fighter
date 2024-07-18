#coding: utf-8

from .character import Character

class Mozarella(Character):
    """Class representing an Mozarella character"""
    def __init__(self, name = False):
        super().__init__(400, 40, 70, 20, name)
