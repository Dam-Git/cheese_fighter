#coding: utf-8

from .character import Character

class Gruyere(Character):
    """Class representing a Gruyere character"""
    def __init__(self, name = False):
        super().__init__(600, 15, 15, 5, name)
