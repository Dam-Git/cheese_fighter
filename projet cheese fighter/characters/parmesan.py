#coding: utf-8

from .character import Character

class Parmesan(Character):
    """Classe qui représente le personnage Parmesan"""
    def __init__(self, name = False):
        super().__init__(300, 30, 15, 40, name)
