#coding: utf-8

from .character import Character

class Parmesan(Character):
    """Class representing a Parmesan character"""
    def __init__(self, name = False):
        super().__init__(300, 30, 15, 40, name)
