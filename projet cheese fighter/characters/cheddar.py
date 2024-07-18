#coding: utf-8

from .character import Character

class Cheddar(Character):
    """Classe qui représente le personnage Cheddar"""
    def __init__(self, name = False):
        super().__init__(300, 80, 30, 50, name)
