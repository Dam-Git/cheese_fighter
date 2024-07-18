#coding: utf-8

from .character import Character

class Gorgonzola(Character):
    """Class representing a Gorgonzola character"""
    def __init__(self, name = False):
        super().__init__(500, 50, 80, 10, name)
